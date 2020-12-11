def data_func(name, surname, date_of_birth, city, email, phone_number):
    try:
        date_of_birth = int(date_of_birth)
        print(
            f"Здравствуйте {name} {surname}! Ваши данные: год рождения - {date_of_birth}; город проживания - {city}; email - {email}; телефон - {phone_number}")
    except ValueError:
        print("Некорректные данные!")

user_name = input("Введите имя: ")
user_surname = input("Введите фамилию: ")
user_date_of_birth = input("Введите год рождения: ")
user_city = input("Введите город проживания: ")
user_email = input("Введите email: ")
user_phone_number = int(input("Введите телефон: "))
data_func(name=user_name, surname=user_surname, date_of_birth=user_date_of_birth, city=user_city, email=user_email,
          phone_number=user_phone_number)
