import os 
from block_markdown import markdown_to_blocks, block_to_block_type
from blocknode import BlockType
from htmlnode import ParentNode, LeafNode 
from textnode import TextNode, text_node_to_html_node
from inline_markdown import text_to_textnodes

def wrap_html(block):

    match block.block_type:
        case BlockType.NORMAL:
            node = ParentNode(
                "p", 
                [
                    text_node_to_html_node(n) 
                    for n in text_to_textnodes(block.block)
                ]
            )
            return node.to_html()

        case BlockType.HEADING:
            heading_number = len(block.block.split(' ')[0])
            node = ParentNode(
                f"h{heading_number}", 
                [
                    text_node_to_html_node(n) 
                    for n in text_to_textnodes(block.block[heading_number + 1:])
                ]
            )
            return node.to_html()

        case BlockType.CODE:
            return (
                ParentNode("pre", 
                    [LeafNode("code", block.block.replace('```', ''))]
                ).to_html()
            ) 

        case BlockType.UNORDEREDLIST:
            text_split = [
                [   text_node_to_html_node(t)
                    for t in text_to_textnodes(b[2:])
                ]
                for b in block.block.split('\n')
            ]
            list_split = [ParentNode('li', ts) for ts in text_split]
            node = ParentNode(
                "ul", 
                list_split
            )
            return node.to_html()

        case BlockType.ORDEREDLIST:
            text_split = [
                [   text_node_to_html_node(t)
                    for t in text_to_textnodes(b[3:])
                ]
                for b in block.block.split('\n')
            ]
            list_split = [ParentNode('li', ts) for ts in text_split]
            node = ParentNode(
                "ol", 
                list_split
            )
            return node.to_html()

        case BlockType.QUOTE:
            return LeafNode("blockquote", block.block.replace('> ', '')).to_html()

        case _:
            raise Exception ("Unknown Block Type")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    final_html = "<div>"
    for block in blocks:
        block_node = block_to_block_type(block)
        final_html += wrap_html(block_node)
    
    return final_html + "</div>"


def extract_heading(markdown):
    if "# " in markdown:
        blocks = markdown_to_blocks(markdown)
        for block in blocks:
            if '# ' in block:
                return block[2:]

    else:
        raise Exception ("No heading")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as f:
        md = f.read()

    with open(template_path, 'r') as f:
        template = f.read()

    content = markdown_to_html_node(md)
    title = extract_heading(md)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    if not(os.path.exists(os.path.dirname(dest_path))):
        os.mkdir(os.path.dirname(dest_path))

    with open(dest_path, 'w') as f:
        f.write(template)
        

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.exists(dir_path_content):
        files = os.listdir(dir_path_content)
        for file in files:
            
            path =os.path.join(dir_path_content, file)

            if os.path.isfile(path):
                generate_page(
                    f"{dir_path_content}/{file}", 
                    template_path, 
                    f"{dest_dir_path}/{file.replace(".md", ".html")}"
                )         
            else:
                print(path)
                generate_pages_recursive( 
                    os.path.join(dir_path_content, file), 
                    template_path, 
                    os.path.join(dest_dir_path, file)
                )

            

    