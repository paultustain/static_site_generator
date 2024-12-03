from enum import Enum

class BlockType(Enum):
    NORMAL = "normal"
    HEADING = "heading"
    QUOTE = "quote"
    CODE = "code"
    UNORDEREDLIST = "unorderedlist"
    ORDEREDLIST = "orderedlist"

class BlockNode():
    def __init__(self, block, block_type):
        self.block = block
        self.block_type = block_type


    def __eq__(self, other):
        return (self.block == other.block) & (self.block_type == other.block_type)


    def __repr__(self):
        return f"BlockNode( {self.block[:11]}... {self.block_type} )"