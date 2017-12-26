'''
@author: Lok
'''

from indexing import Index

class Table():
    
    # For convenience, only strings are allowed for column names and data
    
    def __init__(self, col_names):
        if not isinstance(col_names, tuple):
            raise TypeError("col_names has to be a list of column names")
            
        self.content = Index()
        self.current_pk = 0
        self.col_names = col_names
        self.col_name_indices = Index()
        for col_name in col_names:
            self.col_name_indices.insert((col_name, Index()))
            
        
    def add(self, row):
        if not isinstance(row, tuple):
            raise TypeError("row has to be a tuple of values")
        
        self.content.insert((self.current_pk, row))
        for i in range(len(row)):
            if row[i] != None:
                col_index = self.col_name_indices.find(self.col_names[i])
                col_index[0].insert((row[i], self.current_pk))
        self.current_pk += 1

        
    def remove(self, col_name, value):
        if not col_name in self.col_names:
            raise TypeError("the column name is not legal")
            
        col_index = self.col_name_indices.find(col_name)
        pks = col_index[0].find(value)
        for pk in pks:
            row = self.content.find(pk)[0]
            print (row)
            for i in range(len(row)):
                if row[i] != None:
                    col_index = self.col_name_indices.find(self.col_names[i])
                    pk_list = col_index[0].find(row[i])
                    pk_list.remove(pk)
            self.content.remove(pk)
            
    
    def find(self, col_name, value) -> list:
        if not col_name in self.col_names:
            raise TypeError("the column name is not legal")
            
        col_index = self.col_name_indices.find(col_name)
        pks = col_index[0].find(value)
        rows = []
        for pk in pks:
            rows.append(self.content.find(pk))
        return rows # return a list of tuples(rows)
        
    def lower_bound(self, col_name) -> list:
        if not col_name in self.col_names:
            raise TypeError("the column name is not legal")
            
        index_of_column = self.col_names.index(col_name)
        min = None
        lower_bound = []
        for pk in range(self.current_pk):
            row = self.content.find(pk)[0]
            if len(row) > index_of_column: # ensure the index is less than the length of row
                value = row[index_of_column]
                if min == None or min > value:
                    min = value
                    lower_bound = []
                    lower_bound.append(row)
                elif min == value:
                    lower_bound.append(row)
        return lower_bound # return a list of tuples(rows)
        
    def upper_bound(self, col_name) -> list:
        if not col_name in self.col_names:
            raise TypeError("the column name is not legal")
            
        index_of_column = self.col_names.index(col_name)
        max = None
        upper_bound = []
        for pk in range(self.current_pk):
            row = self.content.find(pk)[0]
            if len(row) > index_of_column: # ensure the index is less than the length of row
                value = row[index_of_column]
                if max == None or max < value:
                    max = value
                    upper_bound = []
                    upper_bound.append(row)
                elif max == value:
                    upper_bound.append(row)
        return upper_bound # return a list of tuples(rows)
    
if __name__ == '__main__':
    # tests start here.
    table = Table(("food", "boolean"))
    table.add(("Beef", "True"))
    table.add(("Pork", "False"))
    table.add(("6", "True"))
    table.add(("6", "False"))
    
    print(table.lower_bound("food"))
    print(table.upper_bound("food"))
    print(table.lower_bound("boolean"))
    print(table.upper_bound("boolean"))
    print()
    
    table.remove("boolean", "True")
    print(table.find("boolean", "False"))
    table.remove("food", "Pork")
    print(table.find("food", "Pork"))
    print(table.find("food", "Beef"))
    print(table.find("boolean", "False"))
        