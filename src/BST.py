"""Implementing a Binary Search tree with In Order Traversal."""


class Node(object):
    def __init__(self, entry, left=None, iterable=None):
        """Node for tree."""
        self.val = entry
        self.left = left
        self.right = iterable


class BinarySearchTree(object):

    def __init__(self, iterable=None):
        # import pdb; pdb.set_trace()
        """This will sety what wwe will be iterating through."""
        self.visited = []
        self.list = []
        self.size = 0
        self.root = None
        if iterable:
            if type(iterable) in [list, tuple]:
                for element in iterable:
                    self.insert(element)

    def insert(self, entry):
        # import pdb; pdb.set_trace()
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
        """."""
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

    def pre_orderTrav(self, entry):
        if entry:
            curr = entry
        else:
            curr = self.root
        yield curr.val
        if curr.left:
            for item in self.inOrderTrav(curr.left):
                yield item
        if curr.right:
            for item in self.inOrderTrav(curr.right):
                yield item

    def preOrder(self):
        for node_data in self.inOrderTrav():
            yield node_data

    def inOrderTrav(self, entry=None):
        if entry:
            curr = entry
        else:
            curr = self.root
        if curr.left:
            for item in self.inOrderTrav(curr.left):
                yield item
        yield curr.val
        if curr.right:
            for item in self.inOrderTrav(curr.right):
                yield item

    def inOrder(self):
        for node_data in self.inOrderTrav():
            yield node_data

    def post_orderTrav(self, entry):
        if entry:
            curr = entry
        else:
            curr = self.root
        if curr.left:
            for item in self.inOrderTrav(curr.left):
                yield item
        if curr.right:
            for item in self.inOrderTrav(curr.right):
                yield item
        yield curr.val

    def postOrder(self):
        for node_data in self.inOrderTrav():
            yield node_data

if __name__ == '__main__':
    import sys
    b = BinarySearchTree([5,3,7,2,8,4,9,1])
    gen = b.inOrder()
    for i in range(5):
        print(next(gen))
