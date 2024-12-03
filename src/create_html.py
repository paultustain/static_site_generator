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
            list_split = [LeafNode('li', b[2:]) for b in block.block.split('\n')]
            node = ParentNode(
                "ul", 
                list_split
            )
            return node.to_html()

        case BlockType.ORDEREDLIST:
            list_split = [LeafNode('li', b[3:]) for b in block.block.split('\n')]
            node = ParentNode(
                "ul", 
                list_split
            )
            return node.to_html()

        case BlockType.QUOTE:
            return LeafNode("quote", block.block.replace('> ', '')).to_html()

        case _:
            raise Exception ("Unknown Block Type")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    final_html = "<div>"
    for block in blocks:
        block_node = block_to_block_type(block)
        final_html += wrap_html(block_node)
    
    return final_html + "</div>"