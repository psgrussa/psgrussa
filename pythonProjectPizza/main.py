import json
import time
import random

orders = {
"Peperoni": 0,
"Cheese": 0,
"Bacon": 0,
"Vegan": 0,
}
with open('orders.json', 'w') as file:
        json.dump(orders, file, indent=4)  # indent=4 для удобного форматировани




products = {
"Chese": random.randint(4,10),
"Testo": random.randint(5,12),
"Peperon": random.randint(3,7),
"Bacn": random.randint(2,6),
"Ovosh": random.randint(2,4)
}
with open('products.json', 'w') as file:
        json.dump(products, file, indent=4)  # indent=4 для удобного форматировани

def secret_menu(username):
    print(f'Здравствуйте, {username} что вы хотите сделать?')
    print('=========================================\n1: Посмотреть остаток продуктов на складе\n2: Изменить цены на пиццы\n3: Вернуться в обычное меню\n=========================================')
    deistv = int(input())
    if deistv == 1:
        with open('products.json', 'r') as file:
            products = json.load(file)
        print(products)
        secret_menu(username)
    elif deistv == 2:
        with open('pizza.json', 'r') as file:
            food = json.load(file)
        print(food)
        Peperoni_2 = int(input('Введите новую цену для Пеперонни: '))
        Cheese_2 = int(input('Введите новую цену для Сырной пиццы: '))
        Bacon_2 = int(input('Введите новую цену для Пиццы с беконом: '))
        Vegan_2 = int(input('Введите новую цену для Веганской пиццы: '))
        pizza = {
            "Peperoni": Peperoni_2,
            "Cheese": Cheese_2,
            "Bacon": Bacon_2,
            "Vegan": Vegan_2
        }
        with open('pizza.json', 'w') as file:
            json.dump(pizza, file, indent=4)  # indent=4 для удобного форматирования
        time.sleep(random.randint(3, 6))
        secret_menu(username)

def func4(username):
    print('Введите пароль для входа в систему')
    correct_password = 1234
    password = int(input())
    if password == correct_password:
        print(f'Добро пожаловать, {username}')
        secret_menu(user)
    else:
        print('Неправильные данные, вход воспрещён')

print('Здравствуйте, это пиццерия мишки фреди чем могу вам помочь?')
def menu():
    with open('products.json', 'r',
              encoding='utf-8') as f:  # encoding='utf-8' важно для корректной обработки кириллицы
        products = json.load(f)
        global Testo
        global Peperon
        global Chese
        global Bacn
        global Ovosh
        Testo = products['Testo']
        Peperon = products['Peperon']
        Chese = products['Chese']
        Bacn = products['Bacn']
        Ovosh = products['Ovosh']
    print('===================== \n1: Заказать пиццу \n2: Заказать напитки \n3: Зарегистрироваться \n4: Я администратор\n5: Общая сумма заказа\n=====================' )
    global func
    func = int(input())

    if func == 4:
        global user
        user = input('Введите имя пользователя: ')
        func4(user)


    if func == 1:
        Peperoni = 0
        Bacon = 0
        Cheese = 0
        Vegan = 0

        print('Вот ваше меню')
        with open('pizza.json', 'r') as file:
            food = json.load(file)
        print(food)
        time.sleep(1.5)
        pos = int(input('Сколько позиций вы хотите заказать? '))
        for i in range(pos):
            order = input('Какую пиццу вы хотите заказать? ')


            if order == 'Peperoni':
                Peperoni = Peperoni+1
                products = {
                    "Testo": Testo-1,
                    "Peperon": Peperon-1,
                    "Chese": Chese-1,
                    "Bacn": Bacn,
                    "Ovosh": Ovosh
                }
                with open('products.json', 'w') as file:
                    json.dump(products, file, indent=4)  # indent=4 для удобного форматировани
                    Testo = Testo-1
                    Peperon = Peperon-1
                    Chese = Chese-1
                    dobav = input('Не хотите ли вы двойной порции пеперони?')
                    if dobav == 'да':
                        print('Хорошо, сейчас принесу')
                        products = {
                            "Peperon": Peperon - 1,
                            "Chese": Chese,
                            "Bacn": Bacn,
                            "Ovosh": Ovosh,
                            "Testo": Testo,
                        }
                        with open('products.json', 'w') as file:
                            json.dump(products, file, indent=4)  # indent=4 для удобного форматировани
            elif order == 'Cheese':
                Cheese = Cheese+1
                products = {
                    "Testo": Testo - 1,
                    "Chese": Chese - 2,
                    "Peperon": Peperon,
                    "Bacn": Bacn,
                    "Ovosh": Ovosh
                }
                with open('products.json', 'w') as file:
                    json.dump(products, file, indent=4)  # indent=4 для удобного форматирования
                    Testo = Testo-1
                    Chese = Chese-2
                    dobav = input('Не хотите ли вы двойной порции сыра?')
                    if dobav == 'да':
                        print('Хорошо, сейчас принесу')
                        products = {
                            "Chese": Chese - 1,
                            "Peperon": Peperon,
                            "Bacn": Bacn,
                            "Ovosh": Ovosh,
                            "Testo": Testo
                        }
                        with open('products.json', 'w') as file:
                            json.dump(products, file, indent=4)  # indent=4 для удобного форматировани
            elif order == 'Bacon':
                Bacon = Bacon+1
                products = {
                    "Bacn": Bacn - 1,
                    "Chese": Chese - 1,
                    "Testo": Testo-1,
                    "Peperon": Peperon,
                    "Ovosh": Ovosh,
                }
                with open('products.json', 'w') as file:
                    json.dump(products, file, indent=4)  # indent=4 для удобного форматирования
                    Bacn = Bacn-1
                    Chese = Chese-1
                    Testo = Testo-1
                    dobav = input('Не хотите ли вы двойной порции бекона?')
                    if dobav == 'да':
                        print('Хорошо, сейчас принесу')
                        products = {
                            "Bacn": Bacn - 1,
                            "Chese": Chese,
                            "Testo": Testo,
                            "Peperon": Peperon,
                            "Ovosh": Ovosh,
                        }
                        with open('products.json', 'w') as file:
                            json.dump(products, file, indent=4)  # indent=4 для удобного форматировани
            elif order == 'Vegan':
                Vegan = Vegan+1
                products = {
                    "Ovosh": Ovosh - 1,
                    "Chese": Chese - 1,
                    "Testo": Testo - 1,
                    "Peperon": Peperon,
                    "Bacn": Bacn
                }
                with open('products.json', 'w') as file:
                    json.dump(products, file, indent=4)  # indent=4 для удобного форматирования
                    Ovosh = Ovosh-1
                    Chese = Chese-1
                    Testo = Testo-1
                    dobav = input('Не хотите ли вы двойной порции овощей?')
                    if dobav == 'да':
                        print('Хорошо, сейчас принесу')
                        products = {
                            "Ovosh": Ovosh - 1,
                            "Chese": Chese,
                            "Testo": Testo,
                            "Peperon": Peperon,
                            "Bacn": Bacn,
                        }
                        with open('products.json', 'w') as file:
                            json.dump(products, file, indent=4)  # indent=4 для удобного форматировани
        print('Спасибо за ваш заказ! Если захотите купить напитков, то позовите меня')
        orders = {
            "Peperoni": Peperoni,
            "Cheese": Cheese,
            "Bacon": Bacon,
            "Vegan": Vegan,
        }
        with open('orders.json', 'w') as file:
            json.dump(orders, file, indent=4)  # indent=4 для удобного форматирования
        menu()


    if func == 2:
        Cola = 0
        Sprite = 0
        Fanta = 0
        Tea = 0
        Orange_juice = 0
        print('Ваше меню')
        time.sleep(0.5)
        with open('drinks.json', 'r') as file:
            drinks = json.load(file)
        print(drinks)
        time.sleep(1.5)
        pos_drinks = int(input('Сколько позиций вы хотите заказать? '))
        for i in range(pos_drinks):
            order_drinks = input('Какие напитки вы хотите заказать? ')
            if order_drinks == 'Cola':
                Cola = Cola+1
            elif order_drinks == 'Sprite':
                Sprite = Sprite+1
            elif order_drinks == 'Fanta':
                Fanta = Fanta+1
            elif order_drinks == 'Tea':
                Tea = Tea+1
            elif order_drinks == 'Orange juice':
                Orange_juice = Orange_juice+1
        print('Спасибо за ваш заказ!')
        orders = {
            "Cola": Cola,
            "Sprite": Sprite,
            "Fanta": Fanta,
            "Tea": Tea,
            "Orange juice": Orange_juice
        }
        with open('orders.json', 'w') as file:
            json.dump(orders, file, indent=4)  # indent=4 для удобного форматирования
        menu()


    if func == 3:
        print('Вы успешно начали регистрацию')
        name = input('Введите ваше имя: ')
        age = int(input('Введите ваш возраст: '))
        if age < 18:
            print('Вы ещё не совершеннолетний')
            menu()
        city = input('Введите город в котором вы находитесь: ')
        print('Проверьте верны ли ваши данные')
        print(f'==================\nИмя - {name}\nВозраст - {age}\nГород - {city}\n==================')
        users = {
            "name": name,
            "age": age,
            "city": city,
        }
        with open('users.json', 'w') as file:
            json.dump(users, file, indent=4)  # indent=4 для удобного форматирования
        menu()
        func = int(input())
        menu()
    elif func == 5:
        with open('pizza.json', 'r', encoding='utf-8') as f:
            price = json.load(f)
        peperoni_price = price['Peperoni']
        cheese_price = price['Cheese']
        bacon_price = price['Bacon']
        vegan_price = price['Vegan']
        with open('orders.json', 'r', encoding='utf-8') as f:
            totil = json.load(f)
        total_peperoni = totil['Peperoni']*peperoni_price
        total_cheese = totil['Cheese']*cheese_price
        total_bacon = totil['Bacon']*bacon_price
        total_vegan = totil['Vegan']*vegan_price
        total = total_bacon+total_vegan+total_cheese+total_peperoni
        print(f'======================\nЧек на {total} рублей\nВыберете способ оплаты\nПо карте      Наличкой\n======================')
        pay = input()
        if pay == 'По карте':
            print('Оплата по карте произведена успешно, хорошего вам дня!')
        elif pay == 'Наличкой':
            print('Оплата наличными получена, хорошего вам дня!')
menu()