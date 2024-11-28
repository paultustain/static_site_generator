class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value=value
        self.children=children
        self.props=props 

    def __eq__(self, other):
        return (self.tag == other.tag) & (self.value == other.value) & (self.children == other.children) & (self.props ==other.props)
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"

    def to_html(self):
        raise NotImplementedError 
    
    def props_to_html(self):
        converted = ''
        if self.props is None:
            return ''
        for k, v in self.props.items():
            converted += f' {k}="{v}"'
        return converted


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props) 

    def to_html(self):
        if self.value is None:
            raise ValueError ("No value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError ("No tag") 
        if self.children is None:
            raise ValueError ("No Children") 
        insert = ''
        for leafnode in self.children:
            insert += leafnode.to_html()

        return f"<{self.tag}{self.props_to_html()}>{ insert }</{self.tag}>"

