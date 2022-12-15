class list(list):
    def mapped(self, function):
        return list(map(function, self))

    def _list_split(self, size, step):
        return list(self[i:i+size] for i in range(0, len(self), step) if size +i <= len(self))

    def chunked(self, size):
        return self._list_split(size, size)

    def window(self,size):
        return self._list_split(size, 1)
