#! /usr/bin/env python3

from textnode import *
#from textnode import TextType
#from textnode import TextNode


def main():
    my_text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(my_text_node)

main()