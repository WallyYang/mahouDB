from indexing import Index
class Table():
    """
    the database table
    self._data: the dictionary(the table) containing all the primary key, each PK has a list(a row)
    self._cols: the list containing all column names, i.e. ("id", "name")
    self._indice: the dictionary containing each value's position
    """

    pk_value = 0

    def __init__(self, cols: list):
        """initialize an empty table with needed columns"""
        self._cols = cols
        self._indices = Index()
        self._data = Index()
        for col_name in cols:
            self._indices.insert((col_name, Index()))

    def add(self, row):
        """
        add a new row into the table
        row as list:
        add each data into the row according to the column order
        row as dict:
        add each pair into the table and column-data
        """
        _row = [None] * len(self._cols)
        if isinstance(row, list):
            for i in range(min(len(self._cols), len(row))):
                _row[i] = row[i]
        elif isinstance(row, dict):
            for i, k in enumerate(self._cols):
                if k in row:
                    _row[i] = row[k]
        else:
            raise "row should be instance of list or map"
        self._data.insert((Table.pk_value,tuple(_row)))
        m = 0
        for col_name in self._cols:
            self._indices._index[col_name][0].insert((_row[m],Table.pk_value))
            m += 1
        Table.pk_value += 1

    def value_find(self, col: str, value: str) -> list:
        """
        find all rows given the column string and value string
        return all corresponding rows appended as a list
        """
        result = self._indices._index[col][0]._index[value]
        ret = []
        for pk in result:
            r = self._data.find(pk)
            ret.append(r)
        return ret

    def value_remove(self, col:str, value: str):
        """remove the row(s) which contain the target value,
        and update the each value's index"""
        del_row = self._indices._index[col][0]._index[value]
        self._indices._index[col][0].remove(value)
        change = {}
        change_time = 0
        for pk in del_row:
            self._data.remove(pk)
            for c in self._indices._index:
                for v in self._indices._index[c][0]._index:
                    for l in range(0,len(self._indices._index[c][0]._index[v])):
                        if self._indices._index[c][0]._index[v][l] == pk:
                            change[str(change_time)] = [c,v,str(l)]
                            change_time += 1
        for changing in change:
            del self._indices._index[(change[changing][0])][0]._index[(change[changing][1])][int(change[changing][2])]
            if len(self._indices._index[(change[changing][0])][0]._index[(change[changing][1])]) == 0:
                self._indices._index[(change[changing][0])][0].remove(change[changing][1])

if __name__ == "__main__":
    table = Table(["id", "name"])
    table.add(["1", "liu"])
    table.add({"id": "2", "name": "wang"})
    table.add({"id": "2", "name": "wang1"})
    table.add({"id": "3", "name": "wang"})
    table.add({"id": "4", "name": "jimmy"})
    table.add({"id": "88", "name": "le"})
    table.value_remove("id","1")
    table.add({"id": "89","name": "tiger"})
    table.add(["9","chang"])
    print(table.value_find("id", "4"))
    print(table.value_find("id","9"))
    list = table._indices._index["name"][0]._index["wang"]
    print(list)
