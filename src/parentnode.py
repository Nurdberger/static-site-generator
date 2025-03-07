from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, node_tag, node_children, node_props=None):
        super().__init__(tag=node_tag, children=node_children, props=node_props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Required tag argument is missing")
        if self.children is None:
            raise ValueError("Required children argument is missing")
        
        html_string = ''
        for child in self.children:
            html_string += child.to_html()
        html_string = f"<{self.tag}>{html_string}</{self.tag}>"
        return html_string