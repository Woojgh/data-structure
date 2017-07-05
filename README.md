README

A set of data structures that allow for the manipulation and implementation of Binary Search Trees.


BST.py

    BinarySearchTree is a class, that accepts a list or tuple of integers or floats on initiation and creates an instance of a Binary search tree.

    *********
    *Methods*
    *********

        *search- Accepts one parameter as integer or float. Will search instance of BST for value and return said Node if found. Returns None if not found. 

        *insert- Accepts one parameter as integer or float. Will create a new Node with given value and insert into the BST properly.

        *breadth_first- Returns a breadth first traversal generator of the current BST.

        *Depth First Traversal*

            *pre_order- Returns a depth first traversal, pre order, generator of the current BST.

            *in_order- Returns a depth first traversal, in order, generator of the current BST.

            *post_order- Returns a depth first traversal, post order, generator of the current BST.
