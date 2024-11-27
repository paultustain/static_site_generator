import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode 


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        htmlnode1 = HTMLNode('tag', 'value', 'child', {"href": "https://www.google.com"})
        htmlnode2 = HTMLNode('other_tag', 'value', 'child', {"href": "https://www.google.com", "target": "__blanks"})
        
        link1 = htmlnode1.props_to_html()
        link2 = htmlnode2.props_to_html()
        self.assertEqual(link1, ' href="https://www.google.com"')
        self.assertEqual(link2, ' href="https://www.google.com" target="__blanks"')
        self.assertNotEqual(htmlnode1, htmlnode2)
        
        leafnode1 = LeafNode("p", "This is a paragraph of text.")
        leafnode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        leafnode3 = LeafNode("a", None) 
        self.assertEqual(leafnode1.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(leafnode2.to_html(), '<a href="https://www.google.com">Click me!</a>')
        with self.assertRaises(ValueError) as ctx:
            leafnode3.to_html()
        self.assertEqual(str(ctx.exception), "No value")

        node1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node2 = ParentNode(
                    None, 
                    [
                        LeafNode("b", "Bold text")
                    ],
                )
        self.assertEqual(node1.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        with self.assertRaises(ValueError) as ctx2:
            node2.to_html()
        self.assertEqual(str(ctx2.exception), "No tag")


        node3 = ParentNode(
                "p", 
                None, 
                )
        with self.assertRaises(ValueError) as ctx3:
            node3.to_html()
        self.assertEqual(str(ctx3.exception), "No Children")

        node4 = ParentNode(
                "q", 
                [
                    LeafNode("a", "Click me!", {"href": "https://www.google.com"}) 
                ], 
                )
        self.assertEqual(node4.to_html(), '<q><a href="https://www.google.com">Click me!</a></q>')
        node5 = ParentNode(
                "p", 
                [
                    LeafNode("p", "This is a paragraph of text."),
                    LeafNode("a", "Click me!", {"href": "https://www.google.com"})
                ], 
                {"style": "NEWSTYLE"}
                )
        self.assertEqual(node5.to_html(), '<p style="NEWSTYLE"><p>This is a paragraph of text.</p><a href="https://www.google.com">Click me!</a></p>')


if __name__ == '__main__':
    unittest.main()
