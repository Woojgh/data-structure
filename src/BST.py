"""Implementing a Binary Search tree with In Order Traversal."""


class Node(object):
    """Class for the data node in our BST."""

    def __init__(self, entry, left=None, iterable=None):
        """Node for tree."""
        self.val = entry
        self.left = left
        self.right = iterable


class BinarySearchTree(object):
    """Class with the containing methods to manipulate and create a BST."""

    def __init__(self, iterable=None):
        """The init will set what we will be iterating through."""
        self.visited = []
        self.list = []
        self.size = 0
        self.root = None
        if iterable:
            if type(iterable) in [list, tuple]:
                for element in iterable:
                    self.insert(element)

    def insert(self, entry):
        """The insert method takes one integer/float and adds it to the BST."""
        if type(entry) not in [float, int]:
            raise TypeError("NUMBERS!!!!! numbers...")
        if not self.root:
            self.root = Node(entry)
            self.size += 1
        else:
            curr = self.root
            while curr:
                if entry > curr.val:
                    if curr.right:
                        curr = curr.right
                        continue
                    else:
                        curr.right = Node(entry)
                        self.size += 1
                elif entry < curr.val:
                    if curr.left:
                        curr = curr.left
                        continue
                    else:
                        curr.left = Node(entry)
                        self.size += 1
                else:
                    return

    def search(self, entry):
        """Search method takes one float/integer and will search the BST for said value."""
        if type(entry) not in [float, int]:
            raise TypeError("NUMBERS!!!!! numbers...")
        else:
            curr = self.root
            while curr:
                if entry > curr.val:
                    if curr.right:
                        curr = curr.right
                        continue
                elif entry < curr.val:
                    if curr.left:
                        curr = curr.left
                        continue
                else:
                    return curr

    def breadth_first(self):
        """Yield a generator for a breadth first traversal."""
        nodes_to_visit = []
        curr = self.root
        nodes_to_visit.append(curr)
        while nodes_to_visit:
            curr = nodes_to_visit.pop(0)
            if curr.left:
                nodes_to_visit.append(curr.left)
            if curr.right:
                nodes_to_visit.append(curr.right)
            yield curr

    def pre_order_trav(self, entry):
        """Helper method to populate a depth first pre order traversal."""
        if entry:
            curr = entry
        else:
            curr = self.root
        yield curr.val
        if curr.left:
            for item in self.pre_order_trav(curr.left):
                yield item
        if curr.right:
            for item in self.pre_order_trav(curr.right):
                yield item

    def pre_order(self):
        """Call method for a generator return on a preorder depth first traversal."""
        for node_data in self.pre_order_trav():
            yield node_data

    def in_order_trav(self, entry=None):
        """Helper method to populate a depth first in order traversal."""
        if entry:
            curr = entry
        else:
            curr = self.root
        if curr.left:
            for item in self.in_order_trav(curr.left):
                yield item
        yield curr.val
        if curr.right:
            for item in self.in_order_trav(curr.right):
                yield item

    def in_order(self):
        """Call method for a generator return on a in order depth first traversal."""
        for node_data in self.in_order_trav():
            yield node_data

    def post_order_trav(self, entry):
        """Helper method to populate a depth first post order traversal."""
        if entry:
            curr = entry
        else:
            curr = self.root
        if curr.left:
            for item in self.post_order_trav(curr.left):
                yield item
        if curr.right:
            for item in self.post_order_trav(curr.right):
                yield item
        yield curr.val

    def post_order(self):
        """Call method for a generator return on a post order depth first traversal."""
        for node_data in self.post_order_trav():
            yield node_data

if __name__ == '__main__':
    b = BinarySearchTree([5, 3, 7, 2, 8, 4, 9, 1])
    gen = b.inOrder()
    for i in range(5):
        print(next(gen))
