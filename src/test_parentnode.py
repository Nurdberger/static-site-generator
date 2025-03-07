import unittest
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html_none_tag(self):
        child = HTMLNode()
        node = ParentNode(None, child)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_none_child(self):
        node = ParentNode("h1", None)
        self.assertRaises(ValueError, node.to_html)
    
    def test_to_html_valid(self):
        child_nodes = [
            LeafNode("b","Bold text"),
            LeafNode(None,"Normal text"),
            LeafNode("i","italic text"),
            LeafNode(None,"Normal text")            
        ]
        node = ParentNode("p",child_nodes)
        expected_result = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_result)