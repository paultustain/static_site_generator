import unittest
from htmlnode import HTMLNode, LeafNode 

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



if __name__ == '__main__':
    unittest.main()