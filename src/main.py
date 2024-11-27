from textnode import TextNode
from htmlnode import HTMLNode

def main():
    tn = TextNode("This is a text node", "bold", "https://boot.dev")
    print(tn)
    hn = HTMLNode('tag', 'value', 'children',
                  {
                    "href": "https://www.google.com", 
                    "target": "_blank",
                            } ) 
    hn.props_to_html()
    print(hn)

if __name__ =='__main__':
    main()
