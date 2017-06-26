'''Constructing the Binary Tree Data Structure'''


class BiTree():

    def __init__(self, root):
        self.left = None
        self.right = None
        self.root = root

    def getLeftChi(self):
        return self.left

    def getRightChi(self):
        return self.right

    def setNodeVal(self, val):
        self.root = val

    def getNodeVal(self):
        return self.root

    def insRight(self, newNode):
        if self.right == None:
            self.right = BiTree(newNode)
        else:
            tree = BiTree(newNode)
            tree.right = self.right
            self.right = tree

    def insLeft(self, newNode):
        if self.left == None:
            self.left = BiTree(newNode)
        else:
            tree = BiTree(newNode)
            tree.left = self.left
            self.left = tree


class Node(object):
    def __init__(self, val, left=None, iterable=None):
        """Node for tree."""
        self.root = val
        self.left = left
        self.right = iterable


class BinarySearchTree():
    if not self._root:
        self._root = Node(val)
        self._size += 1

    else:
        curr = self._root
        while curr:
            if val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(val)
            elif val < curr.val:
                    curr.left = Node(val)
            else:
                return