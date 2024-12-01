from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import (
    text_to_textnodes, 
    split_nodes_image
)

def main():
    pass
    # nodes = text_to_textnodes(
    #     "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
    # )
    # print(nodes)
    # # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    # node = TextNode(
    #     "![image](https://www.example.COM/IMAGE.PNG)",
    #     TextType.NORMAL,
    # )
    # print(split_nodes_image([node]))
if __name__ =='__main__':

    main()
