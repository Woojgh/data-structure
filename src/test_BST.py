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


def test_tree_empty():
    """Instantiate a new Binary tree, that should be an empty list."""
    b = BinarySearchTree([])
    assert b.size == 0


def test_bitr_iter_in_order():
    """Create a Bin tree with an iterable and check it is equal."""
    gen = b.in_order()
    b_list = [item for item in gen]
    assert b_list == [1, 2, 3, 4, 5, 7, 8, 9]


def test_bitr_iter_pre_order():
    """Create a Bin tree with an iterable and check it is equal."""
    gen = b.pre_order()
    b_list = [item for item in gen]
    assert b_list == [5, 3, 2, 1, 4, 7, 8, 9]


def test_bitr_iter_post_order():
    """Create a Bin tree with an iterable and check it is equal."""
    gen = b.post_order()
    b_list = [item for item in gen]
    assert b_list == [1, 2, 4, 3, 9, 8, 7, 5]


