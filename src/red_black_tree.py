class Node():
    def __init__(self, data:tuple, is_black, parent=None, left=None, right=None):
        """Constructor for a Red-Black Tree Node

        Keyword arguments:
        data -- the data in the node
        is_black -- color of the node, True for black, False for Red
        parent -- parent node
        left -- left subtree
        right -- right subtree
        """
        self._data = data
        self._parent = parent
        self._left = left
        self._right = right
        self._is_black = is_black

class Tree():
    """A Red Black Tree for indexing

    root -- the root of the tree
    insert(self, data) -- insert a new data into the tree
    delete(self, data) -- delete a node given the data
    find(self, data) -- find a node given the data
    """


    def __init__(self):
        """Constructor for a Red-Black Tree, with an empty tree"""
        self.root = None

    def insert(self, data):
        pass

    def delete(self, data):
        pass

    def find(self, data):
        pass
