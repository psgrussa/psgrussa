import json
import time
import random
Peperoni = 0
Bacon = 0
Cheese = 0
Vegan = 0
sklad = []
for i in range(1,7):
    sklad.append('Пеперони')
for i in range(2,5):
    sklad.append('Сыр')
for i in range(1,4):
    sklad.append('Овощи')
for i in range(3,12):
    sklad.append('Тесто')
list_orders_pizza = []


def secret_menu(username):
    print(f'Здравствуйте, {username} что вы хотите сделать?')
    print('=========================================\n1: Посмотреть остаток продуктов на складе\n2: Изменить цены на пиццы\n3: Вернуться в обычное меню\n=========================================')
    deistv = int(input())
    if deistv == 1:
        print(sklad)
        time.sleep(random.randint(2,5))
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
            "With Bacon": Bacon_2,
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


def func3():

    name2 = str(input('введите ваше имя:'))
    age2 = int(input('введите ваш возраст:'))
    city2 = str(input('введите город в котором вы живёте:'))
    users = {
        "name": name2,
        "age": age2,
        "city": city2,
    }
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)  # indent=4 для удобного форматирования
    menu()
    func = int(input())


def func1():
    Peperoni = 0
    Bacon = 0
    Cheese = 0
    Vegan = 0
    with open('users.json', 'r') as file:
        user = json.load(file)
    if user == '':
        print('зарегестрируйся')
    else:
        print('какую пиццу вы хотите заказать?')
        with open('pizza.json', 'r') as file:
            pizzas = json.load(file)

            print(pizzas)
        kolvo = int(input('сколько пицц вы хотите заказать? '))
        for i in range(kolvo):
            order = input()
            if order == 'Peperoni':
                Peperoni = Peperoni + 1
            elif order == 'С беконом':
                Bacon = Bacon + 1
            elif order == 'Cheese':
                Cheese = Cheese + 1
            elif order == 'Vegan':
                Vegan = Vegan + 1
        print('Пеперони:', Peperoni)
        print('С беконом:', Bacon)
        print('Сырная:', Cheese)
        print('Веганская:', Vegan)
        orders = {
            "Peperoni": Peperoni,
            "Cheese": Cheese,
            "With bacon": Bacon,
            "Vegan": Vegan
        }
        with open('orders.json', 'w') as file:
            json.dump(orders, file, indent=4)  # indent=4 для удобного форматирования
        menu()
        func = int(input())
        if func == 2:
            fun2()
def fun2():
    print(Peperoni)
    print(Vegan)
    total = Peperoni*500 + Cheese*450 + Bacon*550 + Vegan*350
    print('Общая сумма вашего заказа составляет', total)
print('Здравствуйте, это пиццерия мишки фреди чем могу вам помочь?')
def menu():
    print('===================== \n1: Заказать пиццу \n2: --------- \n3: зарегистрироваться \n4: Я администратор \n=====================' )
menu()
func = int(input())

if func == 4:
    user = input('Введите ваш ник: ')
    func4(user)

if func == 3:
    func3()


elif func == 1:
    func1()







