from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(None, text_node.text, None)
        case TextType.BOLD:
            return LeafNode("b", text_node.text, None)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text, None)
        case TextType.CODE:
            return LeafNode("code", text_node.text, None)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {'href': text_node.url})        
        case TextType.IMAGE:
            return LeafNode("img", "", {'src': text_node.url, 'alt': text_node.text})        
        case _:
            raise ValueError ("Unknown text type")

def main():
    tn = TextNode("This is a text node", "bold", "https://boot.dev")
    print(tn)
    text_node_to_html_node(tn)
    hn = HTMLNode('a', 'value', 'children',
                  {
                    "href": "https://www.google.com", 
                    "target": "_blank",
                            } ) 
    hn.props_to_html()
    print(hn)

if __name__ =='__main__':
    main()
