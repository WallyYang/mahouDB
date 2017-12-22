class Index():
    """
    mock class for indexing

    self._index: a multi-map for {column_value - primary_keys}

    column_value: the value of the column in the table
    primary_key: list containing all the values
    """

    def __init__(self):
        """initialize an empty index"""
        self._index = dict()


    def insert(self, pair: tuple):
        """
        insert a new pair

        pair: tuple(column_value, new_primary_key)
        append primary_key if column exists
        otherwise create a new pair in the dict
        and initialize primary_key as a empty list
        """
        if pair[0] not in self._index:
            # new column_value
            self._index[pair[0]] = list()

        self._index[pair[0]].append(pair[1])


    def remove(self, column_value):
        """
        remove a pair from the index given a column_value
        """
        if column_value in self._index:
            del self._index[column_value]


    def find(self, column_value) -> list:
        """
        find the corresponding primary_keys given a column_value
        return an empty list if not found
        """
        if column_value in self._index:
            return self._index[column_value]
        else:
            return list()
