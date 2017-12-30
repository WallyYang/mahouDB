from indexing import Index

class Table():
    """
    the database table

    self._data: Index<primary_key, row>
    self._cols: tuple(str... ) containing column names i.e. ("id", "name")
    self._indices: Index<col_name, Index<col_vallue, [primary_key]>>

    Table.curr_primary_key: current primary key, use and increment everytime
    """

    curr_primary_key = 1

    def __init__(self, cols: tuple):
        """initialize an empty table with needed columns"""
        self._data = Index()
        self._cols = cols
        self._indices = Index()
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
        pass

    def remove(self, col_name, value):
        pass


    def find(self, col: str, value: str) -> list:
        """
        find all rows given the column string and value string

        return all corresponding rows appended as a list
        """
        pass


    def lower_bound(self, col_name, value):
        pass


    def upper_bound(self, col_name, value):
        pass


    def gen_index(self, col_name):
        pass


    def read_file(self, filename):
        pass


    def write_file(self, filename):
        pass


if __name__ == "__main__":
    table = Table(["id", "name"])
    table.add(["1", "liu"])
    table.add({"id": "2", "name": "wang"})
    table.add({"id": "2", "name": "wang1"})
    print(table.find("id", "2"))
