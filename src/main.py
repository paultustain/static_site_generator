from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import (
    split_nodes_delimiter, 
    split_nodes_link, 
    split_nodes_image
)

def main():
    node = TextNode(
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", 
        TextType.NORMAL
    )
    print(split_nodes_image([node]))
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

if __name__ =='__main__':
    main()
