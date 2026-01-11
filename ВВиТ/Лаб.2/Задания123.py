def main():
    #1.1
    def greet(name):
        return f"Привет, {name}!"
    
    name = input('Введите ваше имя (Или "стоп", чтобы остановить программу):')
    if name.lower() == 'стоп':
        print('Выход из программы')
        return
    print(greet(name))
    
    #1.2
    def square(number):
        return number ** 2
        
    while True:
        number = input('Введите ваше число (Или "стоп", чтобы остановить программу):')
        if number.lower() == 'стоп':
            print('Завершил прогрогрмму!')
            return
        try:
            num = float(number)
            print('Ваше число в квадрате:', square(num))
            break
        except ValueError:
            print('Вы ввели не правильное число')

    #1.3
    def max_of_two(x,y):
        return x if x > y else y
    while True:
        x_input = input('Введите первое число (Или "стоп"): ')
        if x_input.lower() == 'стоп':
            print('Завершил программу!')
            return
        y_input = input('Введите второе число (Или "стоп"): ')
        if y_input.lower() == 'стоп':
            print('Завершил программу!')
            return
        try:
            x = float(x_input)
            y = float(y_input)
            print('Большее число:', max_of_two(x, y))
            break
        except ValueError:
            print('Вы ввели не число, попробуйте снова.')
main()

#2

def describe_person(name, age=30):
    print(f'Имя: {name}, Возраст: {age}')

def main():
    while True:
        name = input('Введите свое имя (Или "стоп" для выхода): ')
        if name.lower() == 'стоп':
            print('Программа офнулась :)')
            return
        
        age_input = input('Введите ваш возраст (не обязательно, Enter = 30): ')
        if age_input.lower() == 'стоп':
            print('Программа офнулась :)')
            return
        
        if age_input == '':  
            describe_person(name)
        else:
            try:
                age = int(age_input)
                describe_person(name, age)
            except ValueError:
                print('Введите пожалуйста число не слово!')
                continue
main()

#3

def is_prime(number):
    if number < 2:
        print(f'{number} - сложное число')
        return False
    for i in range(2, number):
        if number % i == 0:
            print(f'{number} - сложное число')
            return False
    print(f"{number} - простое число")
    return True

while True:
    number = input('Введите ваше число для проверки простого числа(Или стоп для остановки):')
    if number.lower() == 'стоп':
            print('Прога пока')
            break
    try:
        num = int(number)
        is_prime(num)
        print('Ваше число целое!')
    except ValueError:
        print('Ваше число не целое!!!')
        