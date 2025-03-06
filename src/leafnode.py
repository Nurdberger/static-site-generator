from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, leaf_tag, leaf_value, leaf_props=None):
        super().__init__(tag=leaf_tag,
                         value=leaf_value,
                         children=None, 
                         props=leaf_props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        
        match self.tag:
            case None:
                return self.value
            case "a":
                return f'<a{self.props_to_html()}>{self.value}</a>'
            case _:
                return f"<{self.tag}>{self.value}</{self.tag}>"

