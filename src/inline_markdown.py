import re 
from textnode import TextType, TextNode

MARKDOWN_STYLES = {
    "**": TextType.BOLD, 
    "*": TextType.ITALIC, 
    "`": TextType.CODE
}

def format_node(split_node, text_type):
    returned_list = []
    
    for i, n in enumerate(split_node):
        if i % 2 == 0:
            node = TextNode(n, TextType.NORMAL)
        else:
            node = TextNode(n, text_type)
        
        if n != "":
            returned_list.append(
                node
            )
    return returned_list


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    ''' 
    Takes a list of nodes, with a delimiter. 
    This then returns a list with the text split by the delimiter, with 
    the text inside the delimiter converted to text_type.
    TODO - consider how to manage multiple delimiters.
    '''
    output_list = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            output_list.append(node)
            continue
        split_node = node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise ValueError ("Need to close the delimiter")
        
        output_list.extend(format_node(split_node, text_type))
    return output_list


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    
def extract_markdown_links(text):  
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_link(old_nodes):
    output_list = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            output_list.append(node)
            continue
        links = extract_markdown_links(node.text) 
        if node.text == '':
            continue
        if len(links) == 0:
            output_list.append(node)
            continue        
        alt_text = links[0][0]
        link_path = links[0][1]
        split = node.text.split(f"[{alt_text}]({link_path})", 1)
        if split[0] != "":
            output_list.append(
                TextNode(split[0], node.text_type)    
            )
        output_list.append(
            TextNode(alt_text, TextType.LINK, link_path), 
        )
        
        output_list.extend(
            split_nodes_link(
                [
                    TextNode(str(split[1]), node.text_type)
                ]
            )
        )

    return output_list


def split_nodes_image(old_nodes):
    output_list = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            output_list.append(node)
            continue
        links = extract_markdown_images(node.text) 
        if node.text == '':
            return []    
        if len(links) == 0:
            output_list.append(node)
            continue 
        
        alt_text = links[0][0]
        link_path = links[0][1]
        split = node.text.split(f"![{alt_text}]({link_path})", 1)
        if split[0] != "":
            output_list.append(TextNode(split[0], node.text_type))
        
        output_list.append(
            TextNode(alt_text, TextType.IMAGE, link_path), 
        )
        output_list.extend(
            split_nodes_image(
                [
                    TextNode(str(split[1]), node.text_type)
                ]
            )
        )

    return output_list


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    for delim, style in MARKDOWN_STYLES.items():
        nodes = split_nodes_delimiter(nodes, delim, style)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)

    return nodes