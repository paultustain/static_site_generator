import os 
import shutil
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from create_html import generate_pages_recursive, markdown_to_html_node


def move_folder(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    files = os.listdir(src)
    for file in files:
        if os.path.isfile(f"{src}/{file}"):
            shutil.copy(f"{src}/{file}", f"{dst}/{file}")
        else:
            move_folder(f"{src}/{file}", f"{dst}/{file}")


def main():
    move_folder('static', 'public')
    generate_pages_recursive('content', 'template.html', 'public')

    # with open('content/index.md', 'r') as f:
    #     md = f.read()
    # print(markdown_to_html_node(md))

    

if __name__ =='__main__':
    main()
