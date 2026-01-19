class Matrix:
    def __init__(self, rows: int, cols: int):
        self._rows = rows
        self._cols = cols
        # Private data structure
        self._data = [[0 for _ in range(cols)] for _ in range(rows)]

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols

    def set_value(self, row: int, col: int, value: int):
        """Sets a value at a specific coordinate with boundary validation."""
        if 0 <= row < self._rows and 0 <= col < self._cols:
            self._data[row][col] = value
        else:
            raise IndexError("Matrix coordinates out of bounds.")

    def get_data(self):
        """Returns a copy of the data to preserve encapsulation."""
        return [row[:] for row in self._data]

    def __str__(self):
        # Professional formatting with tab spacing
        return "\n".join(["\t".join(map(str, row)) for row in self._data])