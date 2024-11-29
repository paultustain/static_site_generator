import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_link, 
    split_nodes_image
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.NORMAL
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.NORMAL),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.NORMAL
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.NORMAL),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )
    
    def test_split_node_links_none(self):
        node = [
            TextNode(
                "This is a block with no links",
                TextType.NORMAL
            )
        ]
        self.assertListEqual(
            node,
            split_nodes_link(node)
        )

    def test_example_node_links(self):

        node = [TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )]
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.NORMAL),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.NORMAL),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            split_nodes_link(node)
        )

    def test_example_node_links_bold(self):
        node = [TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.BOLD,
        )]
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.BOLD),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.BOLD),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            split_nodes_link(node)
        )

    def test_split_node_images_none(self):
        node = [
            TextNode(
                "This is a block with no images",
                TextType.NORMAL
            )
        ]
        self.assertListEqual(
            node,
            split_nodes_image(node)
        )

    def test_example_node_images(self):

        node = [TextNode(
            "This is text with an image ![to boot dev](https://www.boot.gif) and ![to youtube](https://www.youtube.png)",
            TextType.NORMAL,
        )]
        self.assertListEqual(
            [
                TextNode("This is text with an image ", TextType.NORMAL),
                TextNode("to boot dev", TextType.IMAGE, "https://www.boot.gif"),
                TextNode(" and ", TextType.NORMAL),
                TextNode(
                    "to youtube", TextType.IMAGE, "https://www.youtube.png"
                ),
            ],
            split_nodes_image(node)
        )

    def test_example_node_images_bold(self):
        node = [TextNode(
            "This is text with an image ![to boot dev](https://www.boot.gif) and ![to youtube](https://www.youtube.png)",
            TextType.BOLD,
        )]
        self.assertListEqual(
            [
                TextNode("This is text with an image ", TextType.BOLD),
                TextNode("to boot dev", TextType.IMAGE, "https://www.boot.gif"),
                TextNode(" and ", TextType.BOLD),
                TextNode(
                    "to youtube", TextType.IMAGE, "https://www.youtube.png"
                ),
            ],
            split_nodes_image(node)
        )


if __name__ == "__main__":
    unittest.main()
