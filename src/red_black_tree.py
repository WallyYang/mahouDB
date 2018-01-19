def compare(v1: tuple, v2: tuple) -> int:
    if (v1[0] < v2[0]):
        return -1
    elif (v1[0] > v2[0]):
        return 1
    else:
        return 0 if v1[1] == v2[1] else -1 if v1[1] < v2[1] else 1

class Node():
    def __init__(self,
                 data: tuple,
                 is_black,
                 parent=None,
                 left=None,
                 right=None):
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

    def print_node_dot(self):
        node_name = "node%s" % id(self)
        color = "black" if self._is_black else "red"
        print(""" %s [ label="%s", fillcolor="%s" ];""" % (node_name, self._data, color))

        if self._left != None:
            self._left.print_node_dot()
            print(""" %s -> node%s;""" % (node_name, id(self._left)))
        else:
            print(""" NoneL%s [ shape="box", label="NIL", fontsize="10", fillcolor="black" ];""" % (node_name))
            print(""" %s -> NoneL%s;""" % (node_name, node_name))
        if self._right != None:
            self._right.print_node_dot()
            print(""" %s -> node%s;""" % (node_name, id(self._right)))
        else:
            print(""" NoneR%s [ shape="box", label="NIL", fontsize="10", fillcolor="black" ];""" % (node_name))
            print(""" %s -> NoneR%s;""" % (node_name, node_name))

    def contains(self, data):
        if self._data == data:
            return True
        elif data < self._data:
            if self._left == None:
                return False
            else:
                return self._left.contains(data)
        else:
            if self._right == None:
                return False
            else:
                return self._right.contains(data)

    def min(self):
        check = True
        copy = self
        while check:
            if copy._left != None:
                copy = copy._left
            else:
                check = False
        return copy

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

    def print_tree_dot(self):
        print("digraph {")
        print(""" node [ style="filled", fontcolor="white" ]""")
        if self.root != None:
            self.root.print_node_dot()
        print("}")

    def contains(self, data):
        if self.root == None:
            return False
        else:
            return self.root.contains(data)

    def left_rotate(self, node):
        new_node = node._right
        if node == self.root:
            self.root = new_node
        else:
            if node == node._parent._left:
                node._parent._left = new_node
            else:
                node._parent._right = new_node
        new_node._parent = node._parent
        node._right = new_node._left
        if new_node._left != None:
            new_node._left._parent = node
        new_node._left = node
        node._parent = new_node

    def right_rotate(self, node):
        new_node = node._left
        if node == self.root:
            self.root = new_node
        else:
            if node == node._parent._left:
                node._parent._left = new_node
            else:
                node._parent._right = new_node
        new_node._parent = node._parent
        node._left = new_node._right
        if new_node._right != None:
            new_node._right._parent = node
        new_node._right = node
        node._parent = new_node

    def insert(self, data):
        # reference: CLRS
        if self.root == None:
            self.root = Node(data, True, None)
        else:
            x = self.root
            done = False
            while not done:
                if data < x._data:
                    if x._left == None:
                        x._left = Node(data, False, x)
                        done = True
                    x = x._left
                else:
                    if x._right == None:
                        x._right = Node(data, False, x)
                        done = True
                    x = x._right
            while x._parent != None and x._parent._parent != None and not x._parent._is_black:
                parent = x._parent
                grandparent = parent._parent
                sibling_of_parent = None
                if parent == grandparent._left:
                    sibling_of_parent = grandparent._right
                elif parent == grandparent._right:
                    sibling_of_parent = grandparent._left
                # Case 1
                if sibling_of_parent != None and not sibling_of_parent._is_black:
                    parent._is_black = True
                    sibling_of_parent._is_black = True
                    grandparent._is_black = False
                    x = grandparent
                # Case 2
                elif parent == grandparent._left:
                    if x == parent._right:  # Case 2.5
                        self.left_rotate(parent)
                        # child became parent
                        temp = x
                        x = parent
                        parent = temp
                    parent._is_black = True
                    grandparent._is_black = False
                    # Perform right rotation on grandparent
                    self.right_rotate(grandparent)
                # Case 3
                elif parent == grandparent._right:
                    if x == parent._left:  # Case3.5
                        self.right_rotate(parent)
                        temp = x
                        x = parent
                        parent = temp
                    parent._is_black = True
                    grandparent._is_black = False
                    # Perform left rotation on grandparent
                    self.left_rotate(grandparent)
                # After running Case 2 or 3(right-hand version of 2),
                # parent(x._parent) will be black, the original grandparent and x will be red,
                # the original sibling_of_parent is black since Case 1 is not the case,
                # and the original sibling of x(now a child of original grandparent) is black if its parent is red,
                # which satisfies the rules.
            self.root._is_black = True

    def rb_transplant(self, n1, n2):
        if n1._parent == None:
            self.root = n2
        elif n1 == n1._parent._left:
            n1._parent._left = n2
        else:
            n1._parent._right = n2
        if n2!=None:
            n2._parent = n1._parent

    def find_node(self, data):
        x = self.root
        target = x
        while target._data != data:
            if data < target._data:
                target = x._left
                target._parent = x
                x = x._left
            else:
                target = x._right
                target._parent = x
                x = x._right
        return target

    def delete(self, data):
        del_node = self.find_node(data)
        removed_color = del_node._is_black
        x = None
        if del_node._left == None and del_node._right == None:
            self.rb_transplant(del_node, None)
        elif del_node._left == None:
            x = del_node._right
            self.rb_transplant(del_node, del_node._right)
        elif del_node._right == None:
            x = del_node._left
            self.rb_transplant(del_node, del_node._left)
        else:
            min = del_node._right.min()
            removed_color = min._is_black
            x=min._right
            self.rb_transplant(min, min._right) # The left most node does not have a left child.
            self.rb_transplant(del_node, min)
            
            min._left=del_node._left
            if min._left != None:
                min._left._parent = min
            min._right=del_node._right
            if min._right != None:
                min._right._parent = min
            
            min._is_black=del_node._is_black # Substitute the color

        if removed_color and x != None:
            self.rb_delete_fixup(x)

    def rb_delete_fixup(self, x):
        while x != self.root and x._is_black and x._left != None and x._right != None:
            if x == x._parent._left:
                w = x._parent._right
                # case 1
                if not w._is_black:
                    w._is_black = True
                    x._parent._is_black = False
                    self.left_rotate(x._parent)
                    w = x._parent._right
                # case 2
                if w._left._is_black and w._right._is_black:
                    w._is_black = False
                    x = x._parent
                # case 3
                else:
                    if w._right._is_black:
                        w._left._is_black = True
                        w._is_black = False
                        self.right_rotate(w)
                        w = x._parent._right
                # case 4
                    w._is_black = x._parent._is_black
                    x._parent._is_black = True
                    w._right._is_black = True
                    self.left_rotate(x._parent)
                    x = self.root
            else:
                w = x._parent._left
                if not w._is_black:
                    w._is_black = True
                    x._parent._is_black = False
                    self.right_rotate(x._parent)
                    w = x._parent._left
                if w._right._is_black and w._left._is_black:
                    w._is_black = False
                    x = x._parent
                else:
                    if w._left._is_black:
                         w._right._is_black = True
                         w._is_black = False
                         self.left_rotate(w)
                         w = x._parent._left
                    w._is_black = x._parent._is_black
                    x._parent._is_black = True
                    w._left._is_black = True
                    self.right_rotate(x._parent)
                    x = self.root
        if x != None:
           x._is_black = True

    def find(self, data):
        pass
