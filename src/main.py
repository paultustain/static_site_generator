import os 
import shutil
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from create_html import markdown_to_html_node


def move_folder(src, dst):
    if os.path.exists(dst):
        print("exists")
        shutil.rmtree(dst)
    os.mkdir(dst)
    files = os.listdir(src)
    for file in files:

        if os.path.isfile(f"{src}/{file}"):
            shutil.copy(f"{src}/{file}", f"{dst}/{file}")
        else:
            move_folder(f"{src}/{file}", f"{dst}/{file}")
            
    # if 

def main():
    move_folder('static', 'public')    


    

if __name__ =='__main__':
    main()
