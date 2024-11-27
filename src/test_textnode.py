import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.NORMAL)
        node4 = TextNode("This is a different node", TextType.BOLD)
        node5 = TextNode("Node", TextType.BOLD, "EARL")
        node6 = TextNode("Node", TextType.BOLD, "EARL")
        node7 = TextNode("Node", TextType.BOLD, "EARL2")
        node8 = TextNode("Node", TextType.BOLD, None)
        node9 = TextNode("Node", TextType.BOLD, None)
        self.assertEqual(node, node2)
        self.assertNotEqual(node3, node2)
        self.assertEqual(node5, node6)
        self.assertNotEqual(node6, node7)
        self.assertNotEqual(node4, node2)
        self.assertNotEqual(node6, node2)
        self.assertEqual(node8, node9)

if __name__ == "__main__":
    unittest.main()

