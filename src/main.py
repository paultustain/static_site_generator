from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

from create_html import markdown_to_html_node

def main():
    text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

### This is a heading 3

``` Now I am writing a block of code
it goes over a few
lines 
```

1. Lists
2. are
3. horrible

> now I am quoting something. 

hello
        """
    
    print(markdown_to_html_node(text))
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
