import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)
    
    def test_not_eq(self):
        node1           = TextNode("This is TextNode 1",TextType.NORMAL)
        node1_bold      = TextNode("This is TextNode 1",TextType.BOLD)
        node1_italic    = TextNode("This is TextNode 1",TextType.ITALIC)
        node1_code      = TextNode("This is TextNode 1",TextType.CODE)
        node1_link      = TextNode("This is TextNode 1",TextType.LINK)
        node1_image     = TextNode("This is TextNode 1",TextType.IMAGE)
        node2           = TextNode("This is TextNode 2",TextType.NORMAL)
        node2_bold      = TextNode("This is TextNode 2",TextType.BOLD)
        node2_italic    = TextNode("This is TextNode 2",TextType.ITALIC)
        node2_code      = TextNode("This is TextNode 2",TextType.CODE)
        node2_link      = TextNode("This is TextNode 2",TextType.LINK)
        node2_image     = TextNode("This is TextNode 2",TextType.IMAGE)
        nodes = [node1, node1_bold, node1_italic, node1_code, node1_link, node1_image, node2, node2_bold, node2_italic, node2_code, node2_link, node2_image]

        for test_node in nodes:
            remaining_nodes = nodes.copy()
            remaining_nodes.remove(test_node)
            for comparing_node in remaining_nodes:
                self.assertNotEqual(test_node, comparing_node)
            
        
        


if __name__ == "__main__":
    unittest.main()