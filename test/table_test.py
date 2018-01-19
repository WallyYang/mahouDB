import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from table import Table
import test

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

test.cmp(t2.lower_bound("food", "Beef"), [('Beef', 'True'), ('Pork', 'False')])
test.cmp(t2.upper_bound("food", "Beef"), [('Beef', 'True'), ('6', 'True'), ('6', 'False')])
test.cmp(t2.lower_bound("boolean", "False"), [('Beef', 'True'), ('Pork', 'False'), ('6', 'True'), ('6', 'False')])
test.cmp(t2.upper_bound("boolean", "False"), [('Pork', 'False'), ('6', 'False')])

t2.remove("boolean", "True")
test.cmp(t2.find("boolean", "False"), [('Pork', 'False'), ('6', 'False')])
t2.remove("food", "Pork")
test.cmp(t2.find("food", "Pork"), [])
test.cmp(t2.find("food", "Beef"), [])
test.cmp(t2.find("boolean", "False"), [('6', 'False')])

print("OK")
