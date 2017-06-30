"""Implementing a Binary Search tree with In Order Traversal."""


class Node(object):
    def __init__(self, entry, left=None, iterable=None, parent=None):
        """Node for tree."""
        self.val = entry
        self.left = left
        self.right = iterable
        self.parent = parent


class BinarySearchTree(object):

    def __init__(self, iterable=None):
        # import pdb; pdb.set_trace()
        """This will sety what wwe will be iterating through."""
        self.visited = []
        self.list = []
        self.size = 0
        self.root = None
        self.iterable = iterable
        if iterable is not None:
            if type(iterable) in [list, tuple]:
                for element in iterable:
                    self.list.append(element)
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
                        Node.parent = curr
                elif entry < curr.val:
                    if curr.left:
                        curr = curr.left
                        continue
                    else:
                        curr.left = Node(entry)
                        self.size += 1
                        Node.parent = curr
                else:
                    return

    def search(self, entry):
        """."""
        if type(entry) not in [float, int]:
            raise TypeError("NUMBERS!!!!! numbers...")
        else:
            curr = self.root
            # import pdb; pdb.set_trace()
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
        self.nodes_to_visit = []
        curr = self.root
        self.nodes_to_visit.append(curr)
        while self.nodes_to_visit:
            curr = self.nodes_to_visit.pop(0)
            if curr.left:
                self.nodes_to_visit.append(curr.left)
            if curr.right:
                self.nodes_to_visit.append(curr.right)
            yield curr

    def pre_order_trav(self, entry=None):
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
        for node_data in self.pre_order_trav():
            yield node_data

    def in_order_trav(self, entry=None):
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
        for node_data in self.in_order_trav():
            yield node_data

    def post_order_trav(self, entry=None):
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
        for node_data in self.post_order_trav():
            yield node_data

    def deletion():
        """nope"""
        pass

if __name__ == '__main__':
    b = BinarySearchTree([5, 3, 7, 2, 8, 4, 9, 1])
    gen = b.in_order()
    print([i for i in gen])
