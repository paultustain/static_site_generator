from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import (
    text_to_textnodes, 
    split_nodes_image
)
from block_markdown import markdown_to_blocks

def main():
    text = """
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item

        hello
        """
    
    print(markdown_to_blocks(text))
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
