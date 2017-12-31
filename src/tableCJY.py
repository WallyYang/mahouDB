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
        if len(row) <= len(_row):
            if isinstance(row, list) or isinstance(row, tuple) or isinstance(row, dict):
                if isinstance(row, list) or isinstance(row, tuple):
                    for i in range(min(len(self._cols), len(row))):
                        _row[i] = row[i]
                elif isinstance(row, dict):
                    for k_value in row:
                        if not k_value in self._cols:
                            raise ValueError("Error, the row is not in a correct format.")
                            return
                    for i, k in enumerate(self._cols):
                        if k in row:
                            _row[i] = row[k]
                self._data.insert((Table.pk_value, tuple(_row)))
                m = 0
                for col_name in self._cols:
                    self._indices._index[col_name][0].insert((_row[m], Table.pk_value))
                    m += 1
                Table.pk_value += 1
            else:
                raise TypeError("Error! The row should be an instance of dict, list, or tuple.")
        else:
            raise ValueError("Error! The length should less or equal to the cols.")

    def value_find(self, col: str, value: str) -> list:
        """
        find all rows given the column string and value string
        return all corresponding rows appended as a list
        """
        result = self._indices._index[col][0]._index[value]
        ret = []
        for pk in result:
            r = self._data.find(pk)
            ret += r
        return ret

    def value_remove(self, col:str, value: str):
        """remove the row(s) which contain the target value,
        and update the each value's index"""
        del_row = self._indices._index[col][0]._index[value]
        change = {}
        change_time = 0
        for pk in del_row:
            self._data.remove(pk)
        for c in self._indices._index:
            for v in self._indices._index[c][0]._index:
                first_time = True
                change[str(change_time)] = []
                for pk in del_row:
                    for l in range(0, len(self._indices._index[c][0]._index[v])):
                        if self._indices._index[c][0]._index[v][l] == pk and first_time:
                            change[str(change_time)] = [c, v, l]
                            first_time = False
                            l = len(self._indices._index[c][0]._index[v])
                        elif self._indices._index[c][0]._index[v][l] == pk:
                            change[str(change_time)] += [l]
                            l = len(self._indices._index[c][0]._index[v])
                if len(change[str(change_time)]) != 0:
                    change_time += 1
        for k,v in change.items():
            li = []
            for i in range(2,len(v)):
                li += [v[i]]
            for index in range(0,len(li)):
                del self._indices._index[v[0]][0]._index[v[1]][li[len(li) - 1 - index]]

if __name__ == "__main__":
    table = Table(["id", "name"])
    table.add(["1", "liu"])
    table.add({"id": "2", "name": "wang"})
    table.add({"id": "2", "name": "wang1"})
    table.add({"id": "3", "name": "wang"})
    table.add({"id": "4", "name": "jimmy"})
    table.add(["2","liu"])
    table.add({"id": "88", "name": "le"})
    table.value_remove("name","wang1")
    table.add({"id": "89","name": "tiger"})
    table.add(["9","chang"])
    print(table.value_find("name", "wang1"))
    print(table.value_find("id", "4"))
    print(table.value_find("id","9"))
    print(table.value_find("id", "2"))
    list = table._indices._index["name"][0]._index["wang"]
    print(list)

