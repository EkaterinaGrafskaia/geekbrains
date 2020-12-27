class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row_length = len(self.matrix)
        self.col_length = len(self.matrix[0])

    def __str__(self):
        new_string = []
        for r in range(self.row_length):
            el_string = []
            for c in range(self.col_length):
                el_string.append(str(self.matrix[r][c]))
            new_string.append(' '.join(el_string))
        my_matrix = '\n'.join(str(el) for el in new_string)
        return f"{my_matrix}\n"

    def __add__(self, other):
        new_list = []
        for r in range(self.row_length):
            new_element = []
            for c in range(self.col_length):
                new_element.append(self.matrix[r][c] + other.matrix[r][c])
            new_list.append(new_element)
        return Matrix(new_list)


matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[67, 32], [30, 28], [19, 55]])
print(matrix_1)
print(matrix_1 + matrix_1)
matrix_3 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix_4 = Matrix([[1, 2, 3], [4, 5, 6], [-7, -8, -9]])
print(matrix_3 + matrix_4)
matrix_5 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
matrix_6 = Matrix([[54, 32, 7, 23], [18, 77, 247, -71]])
print(matrix_5 + matrix_6)
