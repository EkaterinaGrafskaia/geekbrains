class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        if self.cell == 0:
            return f"Количество ячеек равно {self.cell}"
        else:
            return f"Количество ячеек равно {self.cell}\n{'*'*self.cell}"

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if (self.cell - other.cell) > 0:
            return Cell(self.cell - other.cell)
        else:
            print("Операция невозможна!")

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def make_order(self,rows):
        num1 = self.cell // rows
        num2 = self.cell % rows
        string = '*' * rows + '\n'
        if num2 == 0:
            return f"{string*num1}"
        if num2 > 0:
            return f"{string*num1}{'*'*num2}"


cell_1 = Cell(35)
cell_2 = Cell(13)
print(cell_1)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(5))
