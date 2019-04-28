

class col_info_stack():

    def __init__(self):
        self._data = []
        self._last = None

    def pop(self):
        if len(self._data) > 0:
            col = self._data.pop()
            if len(self._data) > 0:
                self._last = self._data[-1]
            else:
                self._last = None
            return col
        else:
            return None

    def push(self, info):
        self._data.append(info)
        self._last = info

    def clear(self):
        self._data.clear()

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    @property
    def last(self):
        return self._last