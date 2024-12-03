import unittest
from block_markdown import markdown_to_blocks, block_to_block_type
from blocknode import BlockNode, BlockType

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


    def test_heading1(self):
        block = "# Heading 1"

        self.assertEqual(
            BlockNode(block, BlockType.HEADING), 
            block_to_block_type(block)
        )


    def test_heading4(self):
        block = "#### Heading 4"
        block_to_block_type(block)
        self.assertEqual(
            BlockNode(block, BlockType.HEADING), 
            block_to_block_type(block)
        )


    def test_heading7(self):
        block = "####### No longer a heading"
        self.assertEqual(
            BlockNode(block, BlockType.NORMAL), 
            block_to_block_type(block)
        )


    def test_incorrect_heading(self):
        block = "###43# No longer a heading"
        self.assertEqual(
            BlockNode(block, BlockType.NORMAL), 
            block_to_block_type(block)
        )


    def test_unordered_list(self):
        block = """* item 1
* item 2 
* item 3"""
        self.assertEqual(
            BlockNode(block, BlockType.UNORDEREDLIST), 
            block_to_block_type(block)
        )

    def test_unordered_list2(self):
        block = """- item 1
- item 2 
- item 3"""
        self.assertEqual(
            BlockNode(block, BlockType.UNORDEREDLIST), 
            block_to_block_type(block)
        )

    def test_mixed_list(self):
        block = """- item 1
* item 2"""
        self.assertEqual(
            BlockNode(block, BlockType.NORMAL), 
            block_to_block_type(block)
        )

    def test_ordered_list(self):
        block = """1. item1
2. item3
3. item6"""
        block_to_block_type(block)

    def test_ordered_list_wrong(self):
        block = """1. item1
2. item3
5. item6"""
        block_to_block_type(block)
        # self.assertEqual(
        #     BlockNode(block, BlockType.NORMAL), 
        #     block_to_block_type(block)
        # )
    def test_ordered_list_wrong(self):
        block = """1. item1
f. item3
5. item6"""
        self.assertEqual(
            BlockNode(block, BlockType.NORMAL), 
            block_to_block_type(block)
        )