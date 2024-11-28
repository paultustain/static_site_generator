from textnode import TextType, TextNode


def format_node(split_node, text_type):
    returned_list = []
    for i, n in enumerate(split_node):
        if i % 2 == 0:
            node = TextNode(n, TextType.NORMAL)
        else:
            node = TextNode(n, text_type)
        returned_list.append(
            node
        )
    return returned_list


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    ''' 
    Takes a list of nodes, with a delimiter. 
    This then returns a list with the text split by the delimiter, with 
    the text inside the delimiter converted to text_type.
    TODO - consider how to manage multiple delimiters.
    '''
    output_list = []
    for node in old_nodes:
        split_node = node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise ValueError ("Need to close the delimiter")
        
        output_list.extend(format_node(split_node, text_type))
    return output_list

        
