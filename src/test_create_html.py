import unittest
from create_html import extract_heading


class TestHTMLNode(unittest.TestCase):
    def test_no_heading(self):
        markdown = "Hello"
        with self.assertRaises(Exception) as ctx:
            extract_heading(markdown)
        expected_message = "No heading"
        self.assertEqual(
            str(ctx.exception),
            expected_message
        )

    def test_simple_heading(self):
        markdown = """# This is a header

Some more test here
"""
        self.assertEqual(
            extract_heading(markdown),
            "This is a header"
        )

    def test_low_header(self):
        markdown ="""starting with text

# Moving into a header

But more here.
"""
        self.assertEqual(
            extract_heading(markdown),
            "Moving into a header"
        )