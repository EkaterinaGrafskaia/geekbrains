class Complex:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __str__(self):
        return f"{self.num_1}i + {self.num_2}"

    def __add__(self, other):
        return Complex(self.num_1 + other.num_1, self.num_2 + other.num_2)

    def __mul__(self, other):
        return Complex((self.num_1 * other.num_2 + self.num_2 * other.num_1),
                       (self.num_2 * other.num_2 - self.num_1 * other.num_1))


user_num_11 = int(input("Введите число:"))
user_num_12 = int(input("Введите число:"))
user_num_21 = int(input("Введите число:"))
user_num_22 = int(input("Введите число:"))
complex_1 = Complex(user_num_11, user_num_12)
complex_2 = Complex(user_num_21, user_num_22)
print(complex_1)
print(complex_2)
print(complex_1 + complex_2)
print(complex_1 * complex_2)
