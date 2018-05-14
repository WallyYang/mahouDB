import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from red_black_tree_with_NIL_node import Tree
import test

if __name__ == '__main__':
    tree = Tree()

    tree.insert((10, None))
    tree.insert((3, None))
    tree.insert((14, None))
    tree.insert((17, None))
    tree.insert((24, None))
    tree.insert((42, None))
    tree.insert((0, None))
    tree.insert((25, None))
    tree.insert((43, None))
    tree.insert((45, None))
    tree.insert((46, None))
    tree.insert((44, None))
    tree.insert((26, None))
    tree.insert((222, None))
    tree.insert((90, None))
    tree.insert((55, None))
    
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
    
    # Test case 2
    tree2 = Tree()
    
    tree2.insert((1, "number 1"))
    tree2.insert((17, "number 17"))
    tree2.insert((33, "number 33"))
    tree2.insert((12, "number 12"))
    tree2.insert((151, "number 151"))
    tree2.insert((87, "number 87"))
    tree2.insert((62, "number 62"))
    tree2.insert((98, "number 98"))
    
    test.cmp(tree2.find(17), "number 17")
    test.cmp(tree2.find(151), "number 151")
    test.cmp(tree2.find(62), "number 62")
    test.cmp(tree2.find(151), "number 151")
    
    tree2.delete(87)
    
    lb1 = tree2.lower_bound(20)
    lb1.sort()
    test.cmp(lb1, ["number 151", "number 33", "number 62", "number 98"])
    up1 = tree2.upper_bound(20)
    up1.sort()
    test.cmp(up1, ["number 1", "number 12", "number 17"])
    test.cmp(tree2.range(5, 6), [])
    test.cmp(tree2.range(12, 13), ["number 12"])
    rng3 = tree2.range(0, 160)
    rng3.sort()
    test.cmp(rng3, ["number 1", "number 12", "number 151", "number 17", "number 33", "number 62", "number 98"])
    
    tree2.print_tree_dot()
    