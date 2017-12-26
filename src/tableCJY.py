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
        self._indice = {}
        self._data = {}

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
        self._data[str(Table.pk_value)] = tuple(_row)
        Table.pk_value += 1
        self.update_indice()

    def find(self, col: str, value: str) -> list:
        """
        find all rows given the column string and value string
        return all corresponding rows appended as a list
        """
        i = self._cols.index(col)
        # TODO use index
        ret = []
        for pk in self._data:
            r = self._data[pk]
            if r != None and r[i] == value:
                ret.append(r)
        return ret

    def remove(self, col:str, value: str):
        """remove the row(s) which contain the target value,
        and update the each value's index"""
        i = self._cols.index(col)
        del_row = []
        for pk in self._data:
            r = self._data[pk]
            if r != None and r[i] == value:
                del_row.append(pk)
        for n in range(0,len(del_row)):
            del self._data[(del_row[n])]
        self.update_indice()

    def update_indice(self):
        """update the each value's index which is included in the table"""
        for col in self._cols:
            self._indice[col] = {}
            i = self._cols.index(col)
            for pk in self._data:
                r = self._data[pk]
                if r != None:
                   val = r[i]
                   pk_list = [pk]
                   if not val in self._indice[col]:
                       self._indice[col][val] = pk_list
                   else:
                       self._indice[col][val].append(pk_list)

if __name__ == "__main__":
    table = Table(["id", "name"])
    table.add(["1", "liu"])
    table.add({"id": "2", "name": "wang"})
    table.add({"id": "2", "name": "wang1"})
    table.add({"id": "4", "name": "jimmy"})
    table.add({"id": "88", "name": "le"})
    table.remove("name","wang")
    table.remove("id","88")
    table.add({"id": "89","name": "tiger"})
    table.add(["9","chang"])
    print(table.find("id", "4"))
    print(table.find("id","9"))
    for pk in table._data:
        print(pk)