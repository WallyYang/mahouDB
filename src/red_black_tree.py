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

    def left_rotate(self,node):
        new_node=self._right
        if node==self.root:
            self.root = new_node
        else:
            if node==node.parent.left:
                node._parent._left = new_node
            else:
                node._parent._right = new_node
        new_node._parent=node._parent
        node._right=new_node._left
        new_node._left._parent=node
        new_node._left=node
        node._parent=new_node
        
    def right_rotate(self,node):
        new_node=self._left
        if node==self.root:
            self.root = new_node
        else:
            if node==node.parent.left:
                node._parent._left = new_node
            else:
                node._parent._right = new_node
        new_node._parent=node._parent
        node._left=new_node._right
        new_node._right.parent=node
        new_node._right=node
        node._parent=new_node
    
    def insert(self, data):
        '''
        reference: CLRS
        '''
        if self.root==None:
            self.root=Node(data,True,None)
        else:
            x=self.root
            done=False
            while not done:
                if data<x._data:
                    if x._left==None:
                        x._left=Node(data,False,x)
                        done=True
                    x=x._left
                else:
                    if x._right==None:
                        x._right=Node(data,False,x)
                        done=True
                    x=x._right
            while x._parent!=None and x._parent._parent!=None and not x._parent._is_black:
                parent=x._parent
                grandparent=parent._parent
                sibling_of_parent=None
                if parent==grandparent._left:
                    sibling_of_parent=grandparent._right
                elif parent==grandparent._right:
                    sibling_of_parent=grandparent._left
                # Case 1
                if sibling_of_parent!=None and not sibling_of_parent._is_black:
                    parent._is_black=True
                    sibling_of_parent._is_black=True
                    grandparent._is_black=False
                    x=grandparent
                # Case 2
                elif parent==grandparent._left:
                    if x==parent._right: # Case 2.5
                        self.left_rotate(parent)
                        # child became parent
                        temp=x
                        x=parent
                        parent=temp
                    parent._is_black=True
                    grandparent._is_black=False
                    # Perform right rotation on grandparent
                    self.right_rotate(grandparent)
                # Case 3
                elif parent==grandparent._right:
                    if x==parent._left: # Case3.5
                        self.right_rotate(parent)
                        temp=x
                        x=parent
                        parent=temp
                    parent._is_black=True
                    grandparent._is_black=False
                    # Perform left rotation on grandparent
                    self.left_rotate(grandparent)
                '''
                After running Case 2 or 3(right-hand version of 2), 
                parent(x._parent) will be black, the original grandparent and x will be red, 
                the original sibling_of_parent is black since Case 1 is not the case, 
                and the original sibling of x(now a child of original grandparent) is black if its parent is red, 
                which satisfies the rules.
                '''
            self.root._is_black=True

    def delete(self, data):
        pass

    def find(self, data):
        pass
