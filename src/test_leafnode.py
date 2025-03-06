import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a","Here's the alt text!",{"href":"www.url.com"})
        node_exected_result = "<a href=\"www.url.com\">Here's the alt text!</a>"
        self.assertEqual(node.to_html(), node_exected_result)
    
    def test_leaf_no_value(self):
        node = LeafNode("h1",None)
        self.assertRaises(ValueError,node.to_html)