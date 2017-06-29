"""Test the tree.py module."""
import pytest
from BST import BinarySearchTree


b = BinarySearchTree([5, 3, 7, 2, 8, 4, 9, 1])


@pytest.fixture
def bitr():
    """Init a new Binary Tree."""
    tree = BinarySearchTree()
    return tree


@pytest.fixture
def bitr_iter():
    """Init a new Binary tree from an iterable."""
    gen = b.in_order()
    return gen
