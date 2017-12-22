class Index():
    """
    mock class for indexing

    self._index is a multi-map for {column_value - primary_key}
    primary_key represented by a list containing all the values
    """

    def __init__(self):
        self._index = dict()


    def insert(self, pair: tuple):
        if pair[0] not in self._index:
            # new column_value
            self._index[pair[0]] = list()

        self._index[pair[0]].append(pair[1])


    def remove(self, column_value):
        if column_value in self._index:
            del self._index[column_value]


    def find(self, column_value) -> list:
        if column_value in self._index:
            return self._index[column_value]
        else:
            return list()
