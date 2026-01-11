import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from my_package import ln, log10, log_osn, summ, sq, stepen
import math

def m():
    print("Мат. помощник")
    print("Выберите одно действие")
    
    while True:
        print("\n1. Логарифмы")
        print("2. Математические действия")
        print("3. Выйти из проги")
        
        ch = input("Выберите раздел 1-3")
            
        if ch == "1":
            print("Тут у нас логарифмы")
            print("1. Натуральный логарифм")
            print("2. Десятичный логарифм")
            print("3. Логарифм по основанию")
            log_ch = input('Выберите действие 1-3')
            
            try:
                x = float(input("Ввведиье число:"))
                if log_ch == "1":
                    print(f"результат: {ln(x)}")
                elif log_ch == "2":
                    print(f"результат: {log10(x)}")
                elif log_ch == "3":
                    a = float(input("Введите основание логарифма!"))
                    print(f"результат: {log_osn(x, a)}")
                else:
                    print("неверный выбор")
            except ValueError:
                print("Введено не число")
        
        elif ch == "2":
            print("\nМатематические операции")
            print("1. Сложение")
            print("2. Квадратный корень")
            print("3. Возведение в степень")
            math_ch = input("Выберите действие (1-3): ")

            try:
                if math_ch == "1":
                    a = float(input("Введите первое число: "))
                    b = float(input("Введите второе число: "))
                    print("Результат:", summ(a, b))
                elif math_ch == "2":
                    n = float(input("Введите число: "))
                    print("Результат:", sq(n))
                elif math_ch == "3":
                    a = float(input("Введите число: "))
                    b = float(input("Введите степень: "))
                    print("Результат:", stepen(a, b))
                else:
                    print("Неверный выбор")
            except ValueError:
                print("Введено не число")
        
        elif ch == "3":
            print("Выход из программы.")
            break
        else:
            print("Вы выбрали неверный пункт")
            
m()
