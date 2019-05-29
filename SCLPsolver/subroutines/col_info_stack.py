

class col_info_stack():

    def __init__(self, clear_after=5):
        self._data = []
        self._last = None
        self._clear_after = clear_after

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
        self._auto_clear()

    def clear(self):
        self._data.clear()

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    @property
    def last(self):
        return self._last

    def _auto_clear(self):
        if len(self._data) > self._clear_after:
            cols_to_check = self._data[-self._clear_after:]
            for col in cols_to_check:
                if col.had_resolution or col.alternative is not None:
                    return
            self._data = cols_to_check