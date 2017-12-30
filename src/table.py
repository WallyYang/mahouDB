from indexing import Index

class Table():
    """
    the database table

    self._data: Index<primary_key, row>
    self._cols: tuple(str... ) containing column names i.e. ("id", "name")
    self._indices: Index<col_name, Index<col_vallue, [primary_key]>>
    self._curr_primary_key: current primary key, use and increment everytime
    """

    def __init__(self, cols: tuple):
        """initialize an empty table with needed columns"""
        self._data = Index()
        self._cols = cols
        self._indices = Index()
        self._curr_primary_key = 1
        for col_name in cols:
            self._indices.insert((col_name, Index()))

    def add(self, row):
        """
        add a new row into the table

        row as list:
        add each data into the row according to the column order

        row as tuple:
        add each data into the row according to the column order

        row as dict:
        add each pair into the table and column-data 
        """
        if len(row) <= len(self._cols): # row with the right number of values
            if isinstance(row, tuple):  # row as tuple
                self._data.insert((self._curr_primary_key, row))

            elif isinstance(row, list): # row as list
                self._data.insert((self._curr_primary_key, tuple(row)))

            elif isinstance(row, dict): # row as dictionary

                for k, v in row.items(): # test for  invalid column name
                    if k not in self._cols:
                        raise ValueError("Invalid column name")

                temp = list() # list to be inserted
                for col_name in self._cols: # insert according to column order
                    if col_name in row.keys():
                        temp.append(row[col_name])
                    else:
                        temp.append(None)

                self._data.insert((self._curr_primary_key, tuple(temp)))

            else:
                raise TypeError("Invalid row type, must be tuple, list, or dict")

        else:
            raise ValueError("Invalid Row, number excceeds")

        self._curr_primary_key += 1

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


    def _print(self):
        # print table headings
        print("pk\t", end="")
        for col_names in self._cols:
            print(col_names + "\t", end = "")
        print()

        for pk in self._data._index:
            print(str(pk) + "\t", end = "")
            for value in self._data._index[pk][0]:
                print(str(value) + "\t", end = "")
            print()


if __name__ == "__main__":
    table = Table(["id", "name"])
    table.add(("2", "yang"))
    table.add(["1", "liu"])
    table.add({"id": "2", "name": "wang"})
    table.add({"id": "2", "name": "wang1"})

    table._print()
