import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("This is a text node", TextType.NORMAL)
        node4 = TextNode("This is a different node", TextType.BOLD)
        node5 = TextNode("Node", TextType.BOLD, "EARL")
        node6 = TextNode("Node", TextType.BOLD, "EARL")
        node7 = TextNode("Node", TextType.BOLD, "EARL2")
        node8 = TextNode("Node", TextType.BOLD, None)
        node9 = TextNode("Node", TextType.BOLD, None)
        node10 = TextNode("Link", "link", )
        self.assertEqual(node, node2)
        self.assertNotEqual(node3, node2)
        self.assertEqual(node5, node6)
        self.assertNotEqual(node6, node7)
        self.assertNotEqual(node4, node2)
        self.assertNotEqual(node6, node2)
        self.assertEqual(node8, node9)


        ln1 = text_node_to_html_node(
            TextNode("This is a text node", "bold", "https://boot.dev")
        )
        self.assertEqual(
            ln1,
            LeafNode("b", "This is a text node", None)
        )

        self.assertEqual(
            text_node_to_html_node(node3), 
            LeafNode(None, "This is a text node", None)
        )

        tn1 = TextNode("Link", "link", "https://boot.dev")
        self.assertEqual(
            text_node_to_html_node(tn1), 
            LeafNode('a', "Link", {'href': "https://boot.dev"})
        )

if __name__ == "__main__":
    unittest.main()

