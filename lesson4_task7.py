n = int(input("Enter the last number: "))


# ------------------без yield-------------------
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


for el in range(1, n):
    print(fact(el))


# ----------------------------------------------
def fact(n):
    s = 1
    for i in range(1, n):
        s = s * i
        yield s


for el in fact(n):
    print(el)
