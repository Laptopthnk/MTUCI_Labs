from my_mudule import summa
while True:
    try:
        x = float(input("Введите первое число:"))
        y = float(input("Введите второе число:"))
        result = summa(x,y)
        print("Сумма чиссел:", result)
        break
    except ValueError:
        print("Введено не число!")
        
    
    
