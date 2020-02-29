class Board:
    columns = -1
    rows = -1
    grid = None

    def __init__(self, rows, columns):
        if rows <= 0 or columns <= 0:
            raise ValueError

        self.rows = rows
        self.columns = columns
        self.grid = [[' ' for i in range(columns)] for j in range(rows)]

    def to_string(self):
        print(self.rows)
        print('============ Whites (v) ============')
        print('Captured:')
        print('9:')
        col_indices = '   '
        for i in range(self.columns):
            col_indices += ' ' + str(i) + ' '
        print(col_indices)
        print('+ ' + ' -' * len(col_indices) + ' +')
        for index, row in enumerate(self.grid):
            row_string = str(index) + '| '
            for position in row:
                row_string += position + ' '
            print(row_string)
        print('+' + ' -' * len(col_indices) + ' +')
        print('Captured:')
        print('9:')
        print('============ Blacks (^) ============')
