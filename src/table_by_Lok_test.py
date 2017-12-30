from table_by_Lok import Table
import test

t = Table(("id", "name", "loc", "note"))

t.add(("1","wally"))
t.add(("2","wally2","18"))
t.add(("3","wally3","tom"))
t.add(("4","wally4","tom", "hello"))
t.add(("4","wally42","tom", "hello"))
t.add(("4","wally43","tom"))
test.cmp(t.find("id", "1"), [("1","wally",None,None)])
test.cmp(t.find("id", "4"), [("4","wally4","tom", "hello"), ("4","wally42","tom", "hello"),("4","wally43","tom", None)])

t.remove("id", "4")
test.cmp(t.find("id", "4"), [])
