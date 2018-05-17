import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from table import Table
import test
import time
import random

# Test case 1
t1 = Table(("id", "name", "loc", "note"))

t1.add(("1", "wally"))
t1.add(("2", "wally2", "18"))
t1.add(("3", "wally3", "tom"))
t1.add(("4", "wally4", "tom", "hello"))
t1.add(("4", "wally42", "tom", "hello"))
t1.add(("4", "wally43", "tom"))

t1.write_file(os.path.abspath(os.path.dirname(__file__))+'\data.bin')
t1.read_file(os.path.abspath(os.path.dirname(__file__))+'\data.bin')

test.cmp(t1.find("id", "1"), [("1", "wally", None, None)])
test.cmp(t1.find("id", "4"), [("4", "wally4", "tom", "hello"), ("4", "wally42", "tom", "hello"), ("4", "wally43", "tom", None)])
test.cmp(t1.find("loc", "18"), [("2", "wally2", "18", None)])
test.cmp(t1.find("note", "hello"), [("4", "wally4", "tom", "hello"), ("4", "wally42", "tom", "hello")])

t1.remove("id", "4")
test.cmp(t1.find("id", "4"), [])

test.cmp(t1.find("id", "5"), [])
test.cmp(t1.find("name", "y"), [])

t1.remove("id", "5")
t1.remove("note", "5")

# Test case 2
t2 = Table(("food", "boolean"))

t2.add(("Beef", "True"))
t2.add(("Pork", "False"))
t2.add(("6", "True"))
t2.add(("6", "False"))


lb = t2.lower_bound("food", "Beef")
lb.sort()
test.cmp(lb, [('Beef', 'True'), ('Pork', 'False')])
ub = t2.upper_bound("food", "Beef")
ub.sort()
test.cmp(ub, [('6', 'False'), ('6', 'True'), ('Beef', 'True')])

lb = t2.lower_bound("boolean", "False")
lb.sort()
test.cmp(lb, [('6', 'False'), ('6', 'True'), ('Beef', 'True'), ('Pork', 'False')])
ub = t2.upper_bound("boolean", "False")
ub.sort()
test.cmp(ub, [('6', 'False'), ('Pork', 'False')])

rng = t2.range("boolean", "False", "True")
rng.sort()
test.cmp(rng, [('6', 'False'), ('6', 'True'), ('Beef', 'True'), ('Pork', 'False')])
test.cmp(t2.range("food", "C", "D"), [])

t2.remove("boolean", "True")
test.cmp(t2.find("boolean", "False"), [('Pork', 'False'), ('6', 'False')])
t2.remove("food", "Pork")
test.cmp(t2.find("food", "Pork"), [])
test.cmp(t2.find("food", "Beef"), [])
test.cmp(t2.find("boolean", "False"), [('6', 'False')])

# Advanced test 1 (10^6 row 3 columns)
print("Advanced Test 1")
COUNT = 1000000

t = time.process_time()
current_t = time.process_time()
col_names = ("n", "reverse_n", "n_is_odd")
at1 = Table(col_names)
current_t = time.process_time() - current_t
print("Time Use: " + str(current_t) + "s for initiation.")
sys.stdout.flush()

reverse_count = COUNT
for i in range(COUNT):
    at1.add((str(i), str(COUNT - i), str(i % 2 == 1)))
    reverse_count -= 1
    
current_t = time.process_time() - current_t
print("Time Use: " + str(current_t) + "s for adding.")
sys.stdout.flush()

for i in range(COUNT):
    test.cmp(at1.find("n", str(i)), [(str(i), str(COUNT - i), str(i % 2 == 1))])
current_t = time.process_time() - current_t
print("Time Use: " + str(current_t) + "s for finding.")
sys.stdout.flush()
    
for i in range(COUNT):
    at1.remove("n", str(i))
current_t = time.process_time() - current_t
print("Time Use: " + str(current_t) + "s for removing.")
sys.stdout.flush()

test.cmp(at1.content._index.root, None)
for col_name in col_names:
    test.cmp(at1.col_name_indices._index.find(col_name)[0]._index.root, None)
print("Total time use: " + str(time.process_time() - t) + "s.\n")
sys.stdout.flush()

print("OK")
