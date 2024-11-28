from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


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
