from red_black_tree_with_NIL_node import Tree

class Index():
    """
    class for indexing with red black tree

    self._index: a multi-map for {column_value - primary_keys}

    column_value: the value of the column in the table
    primary_key: list containing all the values
    """
    
    def __init__(self):
        """initialize an empty index"""
        self._index = Tree()


    def insert(self, pair: tuple):
        """
        insert a new pair

        pair: tuple(column_value, new_primary_key)
        append primary_key if column exists
        otherwise create a new pair in the dict
        and initialize primary_key as a empty list
        """
        if not self._index.contains(pair[0]):
            self._index.insert((pair[0], list()))

        node = self._index.find_node(pair[0])
        node._data[1].append(pair[1])


    def remove(self, column_value):
        """
        remove a pair from the index given a column_value
        """
        if self._index.contains(column_value):
            self._index.delete(column_value)


    def find(self, column_value) -> list:
        """
        find the corresponding primary_keys given a column_value
        return an empty list if not found
        """
        list = self._index.find(column_value)
        if list is None:
            list = []
        return list
        
        
    def keys(self):
        return self._index.keys()
        
        
    def lower_bound(self, value):
        return self._index.lower_bound(value)
        
        
    def upper_bound(self, value):
        return self._index.upper_bound(value)
        
        
    def range(self, lower_bound, upper_bound):
        return self._index.range(lower_bound, upper_bound)
        