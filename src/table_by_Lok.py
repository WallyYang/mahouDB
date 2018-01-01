'''
@author: Lok
'''

import os
from indexing import Index

class Table():
    """
    the database table
    self.content: Index<primary_key, row>
    self.col_names: tuple(str... ) containing column names i.e. ("id", "name")
    self.col_name_indices: Index<col_name, Index<col_vallue, [primary_key]>>
    self.current_pk: current primary key, use and increment everytime
    """
    
    # For convenience, only strings are allowed for column names and data
    
    def __init__(self, col_names: tuple):
        """initialize an empty table with needed columns"""
        if not isinstance(col_names, tuple):
            raise TypeError("col_names has to be a list of column names")
            
        self.content = Index()
        self.current_pk = 0
        self.col_names = col_names
        self.col_name_indices = Index()
        for col_name in col_names:
            self.col_name_indices.insert((col_name, Index()))
        
    def add(self, row: tuple):
        """
        add a new row into the table
        row as list:
        add each data into the row according to the column order
        
        row as dict:
        add each
        """
        if not isinstance(row, (tuple, dict)):
            raise TypeError("row has to be a tuple of a dict of values")
        
        if isinstance(row, dict):
            for key in row.keys():
                if not key in self.col_names:
                    raise Exception("the column name is not legal")
            
            realRow = []
            for col_name in self.col_names:
                if col_name in row.keys():
                    realRow.append(row.get(col_name))
                else:
                    realRow.append(None)
            row = realRow
        else:
            # Format the row. Delete extra columns.
            rowList = []
            for i in range(len(self.col_names)):
                if i < len(row):
                    rowList.append(row[i])
                else:
                    rowList.append(None)
            row = tuple(rowList)
            
        self.content.insert((self.current_pk, row))
        for i in range(len(row)):
            if row[i] != None:
                col_index = self.col_name_indices.find(self.col_names[i])
                col_index[0].insert((row[i], self.current_pk))
        self.current_pk += 1
        
    def remove(self, col_name, value):
        if not col_name in self.col_names:
            raise Exception("the column name is not legal")
            
        col_index = self.col_name_indices.find(col_name)
        pks = col_index[0].find(value)
        pks = tuple(pks) # avoid alias
        for pk in pks:
            row = self.content.find(pk)[0]
            for i in range(len(row)):
                if row[i] != None:
                    col_index = self.col_name_indices.find(self.col_names[i])
                    pk_list = col_index[0].find(row[i])
                    pk_list.remove(pk)
            self.content.remove(pk)
            
    def find(self, col_name, value) -> list:
        """
        find all rows given the column string and value string
        return all corresponding rows appended as a list
        """
        if not col_name in self.col_names:
            raise Exception("the column name is not legal")
            
        col_index = self.col_name_indices.find(col_name)
        pks = col_index[0].find(value)
        rows = []
        for pk in pks:
            rows.extend(self.content.find(pk))
        return rows # return a list of tuples(rows)
        
    def lower_bound(self, col_name, value) -> list:
        if not col_name in self.col_names:
            raise Exception("the column name is not legal")
        if value == None:
            raise TypeError("the value cannot be None")
            
        index_of_column = self.col_names.index(col_name)
        return_range = []
        for pk in self.content._index.keys():
            row = self.content.find(pk)[0]
            if row[index_of_column] != None: # ensure the index is less than the length of row
                this_value = row[index_of_column]
                if this_value >= value:
                    return_range.append(row)
        return return_range # return a list of tuples(rows)
        
    def upper_bound(self, col_name, value) -> list:
        if not col_name in self.col_names:
            raise Exception("the column name is not legal")
        if value == None:
            raise TypeError("the value cannot be None")
            
        index_of_column = self.col_names.index(col_name)
        return_range = []
        for pk in range(self.current_pk):
            row = self.content.find(pk)[0]
            if row[index_of_column] != None: # ensure the index is less than the length of row
                this_value = row[index_of_column]
                if this_value <= value:
                    return_range.append(row)
        return return_range # return a list of tuples(rows)

    def write_file(self, filename):
        """
        output the data to filename with the following binary format:
        
        -> current_pk \xFF len(col_names) \xFF {col_name \xFF} {pk \xFF {cell element \xFF}}
        """
        print(os.getcwd())
        out_data = open(filename, 'wb')
        out_data.write(str(self.current_pk).encode('utf8'))
        out_data.write(b'\xff')
        out_data.write(str(len(self.col_names)).encode('utf8'))
        out_data.write(b'\xff')
        
        for col_name in self.col_names:
            out_data.write(col_name.encode('utf8'))
            out_data.write(b'\xff')
        
        for pk in self.content._index.keys():
            out_data.write(str(pk).encode('utf8'))
            out_data.write(b'\xff')
            row = self.content.find(pk)[0]
            for element in row:
                if element != None:
                    out_data.write(element.encode('utf8'))
                out_data.write(b'\xff')
        out_data.close()
    
if __name__ == '__main__':
    # tests start here.
    table = Table(("food", "boolean"))
    table.add(("Beef", "True"))
    table.add(("Pork", "False"))
    table.add(("6", "True"))
    table.add(("6", "False"))
    table.write_file('C:\mahouDB\src\data.bin')
    
    print(table.lower_bound("food", "Beef"))
    print(table.upper_bound("food", "Beef"))
    print(table.lower_bound("boolean", "False"))
    print(table.upper_bound("boolean", "False"))
    print()
    
    table.remove("boolean", "True")
    print(table.find("boolean", "False"))
    table.remove("food", "Pork")
    print(table.find("food", "Pork"))
    print(table.find("food", "Beef"))
    print(table.find("boolean", "False"))
        