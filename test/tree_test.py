import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from red_black_tree_with_NIL_node import Tree

if __name__ == '__main__':
    tree = Tree()

    tree.insert(10)
    tree.insert(3)
    tree.insert(14)
    tree.insert(17)
    tree.insert(24)
    tree.insert(42)
    tree.insert(0)
    tree.insert(25)
    tree.insert(43)
    tree.insert(45)
    tree.insert(46)
    tree.insert(44)
    tree.insert(26)
    tree.insert(222)
    tree.insert(90)
    tree.insert(55)
    tree.delete(24)
    tree.delete(44)
    tree.delete(45)
    tree.delete(43)
    tree.delete(10)
    tree.delete(14)
    tree.delete(42)
    tree.delete(46)
    tree.delete(17)
    tree.delete(26)
    tree.delete(3)
    tree.delete(0)
    tree.delete(25)
    tree.delete(90)
    tree.print_tree_dot()