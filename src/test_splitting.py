import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        unfinished_node = TextNode("This is an **unfinished node", TextType.NORMAL)
        with self.assertRaises(ValueError) as ctx:
            split_nodes_delimiter([unfinished_node], '**', TextType.BOLD)
            self.assertEqual(str(ctx.exception), "Need to close the delimiter")

        bold_node = TextNode("This is a **finished** node", TextType.NORMAL)
        self.assertEqual(
            split_nodes_delimiter([bold_node], "**", TextType.BOLD), 
            [
                TextNode("This is a ", TextType.NORMAL),
                TextNode("finished", TextType.BOLD),
                TextNode(" node", TextType.NORMAL),
            ]
        )

        code_node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        self.assertEqual(
            split_nodes_delimiter([code_node], "`", TextType.CODE), 
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.NORMAL),
            ]
        )

        double_ital =  TextNode("This is *text* with *two italic* blocks", TextType.NORMAL)
        self.assertEqual(
            split_nodes_delimiter([double_ital], "*", TextType.ITALIC), 
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.ITALIC),
                TextNode(" with ", TextType.NORMAL),
                TextNode("two italic", TextType.ITALIC),
                TextNode(" blocks", TextType.NORMAL),
            ]
        )

        full_node = TextNode("*full*", TextType.NORMAL)
        self.assertEqual(
            split_nodes_delimiter([full_node], "*", TextType.ITALIC), 
            [
                TextNode("", TextType.NORMAL),
                TextNode("full", TextType.ITALIC),
                TextNode("", TextType.NORMAL),
            ]
        )

        end_node = TextNode("This node ends **bold**", TextType.NORMAL)
        self.assertEqual(
            split_nodes_delimiter([end_node], "**", TextType.BOLD), 
            [
                TextNode("This node ends ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
                TextNode("", TextType.NORMAL),
            ]
        )

        self.assertEqual(
            extract_markdown_images(
                "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
            ), 
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        )

        self.assertEqual(
            extract_markdown_links(
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
            ), 
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        )