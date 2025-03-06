class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        strings = []
        for key in self.props.keys():
            strings.append(f'{key}="{self.props[key]}"')
        html_string = " " + " ".join(strings)
        return html_string

