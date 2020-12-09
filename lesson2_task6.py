products = []
analytics = {}
name = []
price = []
amount = []
unit = []
product_name = input("Введите название первого товара: ")
product_price = int(input("Введите цену первого товара: "))
product_amount = int(input("Введите количество первого товара: "))
product_unit = input("Введите единицы измерения первого товара: ")
dict = {"название": product_name, "цена": product_price, "количество": product_amount, "eд": product_unit}
products.append((1, dict))
n = 1
while True:
    question = input("Вы хотите добавить еще один товар?(Введите Y или N): ")
    if question == "N":
        for i in range(len(products)):
            if products[i][1]['название'] not in name:
                name.append(products[i][1]['название'])
            if products[i][1]['цена'] not in price:
                price.append(products[i][1]['цена'])
            if products[i][1]['количество'] not in amount:
                amount.append(products[i][1]['количество'])
            if products[i][1]['eд'] not in unit:
                unit.append(products[i][1]['eд'])
            else:
                continue
        analytics = {"название": name, "цена": price, "количество": amount, "eд": unit}
        print(analytics)
        break
    if question == "Y":
        n += 1
        product_name = input("Введите название товара: ")
        product_price = int(input("Введите цену товара: "))
        product_amount = int(input("Введите количество товара: "))
        product_unit = input("Введите единицы измерения товара: ")
        dict = {"название": product_name, "цена": product_price, "количество": product_amount, "eд": product_unit}
        products.append((n, dict))
    else:
        print("Я Вас не понимаю. Попробуйте еще раз!")
        continue
