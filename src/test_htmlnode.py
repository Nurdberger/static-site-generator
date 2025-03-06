import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode(tag="Tag1",value="Value1", props={"prop1":"prop_value1", "prop2":"prop_value2"})
        expected_result = ' prop1="prop_value1" prop2="prop_value2"'
        print(f"Expecting\t: {expected_result}")
        print(f"Actual\t\t: {node1.props_to_html()}")
        self.assertEqual(node1.props_to_html(), expected_result)



if __name__ == "__main__":
    unittest.main()
