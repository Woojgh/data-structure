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

    def depth_first(self, entry):
        if entry is None:
            return 0
        left_depth = self.depth_first(entry.left)
        right_depth = self.depth_first(entry.right)
        if (left_depth > right_depth):
            return left_depth + 1
        return right_depth + 1

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

    def check_that_balance(self, target):
        """check the balance of your treeeee"""
        if self.size == 0:
            return 0
        if not target:
            target = self.root
        else:
            target = self.search(target)
        return self.depth_first(target.right) - self.depth_first(target.left)

    def find_min_depth(self, target):
        curr = target
        while curr.left is not None:
            curr = curr.left
        return curr

    def find_max_depth(self, target):
        curr = target
        while curr.right is not None:
            curr = curr.right
        return curr

    def deletion(self, entry, entry_exist=None):
        """nope"""
        self.search(entry)
        if entry.exist is None:
            return 'This is the end of all that you know!'
        elif entry_exist:
            if entry.left is None and entry.right is None:
                self.pop(entry)
            elif entry.left and not entry.right:
                self.entry.val = self.entry.left.val
                self.pop(entry.left)
            elif entry.right and not entry.left:
                self.entry.val = self.entry.right.val
                self.pop(entry.right)
        elif self.search(entry):
            return self.deletion(entry, True)
        else:
            return 'Cannot delete what does not exist'
            """Search for node target
            if no target exists, then we break function and return none.
            if target exists, do a balance check.
            insert node to check and check thenlength of left and right child.
            subtract the smaller from the larger, that is our child tree to look for node replacment.
                if left child, we get the right most grandchild. if right most child has left child, assign the child to rightmost grandchild parent
                if right child, we get left most grand child. if left most child has left child, assign the child to leftmost grandchild parent
            which ever child tree is used, take that result and replace target node with result.
"""

if __name__ == '__main__':  # pragma: no cover
    b = BinarySearchTree([5, 3, 7, 2, 8, 4, 9, 1])
    gen = b.in_order()
    print([i for i in gen])
