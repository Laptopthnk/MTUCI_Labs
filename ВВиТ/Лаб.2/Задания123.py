# 1 задание:
def greet(name):
    return f"Привет, {name}!"
name = input("Введите имя: ")
print(greet(name))

# 2 задание:
def square(number: int) -> int:
    return number ** 2
number = int(input("Введите число: "))
print("Квадрат числа:", square(number))

# 3 задание:
def max_of_two(x,y):
    if x > y:
        return x
    else:
        return y
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
result = max_of_two(number1, number2)
print("Наибольшее число: ", result)


# 4 задание:
def describe_person(name:str, age: int=30)-> None:
    return f"Меня зовут {name}, мне {age} лет"

username = input("Введите имя: ") or name
user_age = input("Введите возраст: ")
if user_age:
    print(describe_person(username, user_age))
else:
    print(describe_person(username))


    print("Имя:", username)
    print("Возраст:", user_age)


# 5 задание:
def prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
number = int(input("Введите число: "))
if prime(number):
    print("Число простое")
else:
    print("Число не простое")
