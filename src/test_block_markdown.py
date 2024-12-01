import unittest
from block_markdown import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_default_block_test(self):
        text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
        """

        self.assertListEqual(
            [
                "# This is a heading", 
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", 
                """* This is the first list item in a list block\n* This is a list item\n* This is another list item"""
            ], 
            markdown_to_blocks(text)
        )

    def test_default_block_blanks(self):

        text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item





# Heading 2
        """

        self.assertListEqual(
            [
                "# This is a heading", 
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", 
                """* This is the first list item in a list block\n* This is a list item\n* This is another list item""", 
                "# Heading 2"
            ], 
            markdown_to_blocks(text)
        )