from blocknode import BlockNode, BlockType


def markdown_to_blocks(markdown):
    inlines = markdown.split('\n\n')
    return [line.strip() for line in inlines if line.strip() != '']


def block_to_block_type(block):
    split_block = block.split(' ')
    if split_block[0] == ('#' * len(split_block[0])):
        if len(split_block[0]) > 6:
            return BlockNode(block, BlockType.NORMAL)
        return BlockNode(block, BlockType.HEADING)
    elif split_block[0] == '>':
        return BlockNode(block, BlockType.QUOTE)
    elif split_block[0] == '```':
        return BlockNode(block, BlockType.CODE)
    elif split_block[0] == '*':
        if all([v[0] == '*' for v in block.split('\n')]):
            return BlockNode(block, BlockType.UNORDEREDLIST)
        else:
            return BlockNode(block, BlockType.NORMAL)
    elif split_block[0] == '-':
        if all([v[0] == '-' for v in block.split('\n')]):
            return BlockNode(block, BlockType.UNORDEREDLIST)
        else:
            return BlockNode(block, BlockType.NORMAL)
    elif split_block[0] == '1.':
        try:
            numbers = [int(v[0]) for v in block.split('\n')]
        except ValueError:
            return BlockNode(block, BlockType.NORMAL)
        if all([numbers[i] == (numbers[i+1] - 1) for i in range(len(numbers) -1)]):
            return BlockNode(block, BlockType.ORDEREDLIST)
    else:
        return BlockNode(block, BlockType.NORMAL)

