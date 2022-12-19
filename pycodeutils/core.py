from collections.abc import Iterable


class list(list):
    def mapped(self, function):
        return list(map(function, self))

    def _list_split(self, size, step):
        return self(
            self[i : i + size]
            for i in range(0, len(self), step)
            if size + i <= len(self)
        )

    def chunked(self, size):
        return self._list_split(size, size)

    def window(self, size):
        return self._list_split(size, 1)


class set(set):
    def __add__(self, element) -> set:
        if type(element) == set:
            return set(self.union(element))
        elif isinstance(element, Iterable):
            return set(self.union(set(element)))
        return set(self.union(set([element])))
