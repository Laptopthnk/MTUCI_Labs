import math

def ln(x):
    if x <= 0:
        return "Число должно быть больше нуля"
    return math.log(x)

def log10(x):
    if x <= 0:
        return "ошибка: число должно быть > 0"
    return math.log10(x)

def log_osn(x, a):
    if x <= 0 or a <= 0 or a == 1:
        return "Ошибка: числа должны быть больше нуля, а основание = 1"
    return math.log(x, a)
