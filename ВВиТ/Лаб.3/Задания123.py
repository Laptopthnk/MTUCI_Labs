1 ЗАДАНИЕ
Чтение всего файла

with open('C:/Users/andrey/Desktop/example.txt', 'r') as file:
    content = file.read()
    print(content)

Чтение строк
with open('C:/Users/andrey/Desktop/example.txt', 'r') as file:
    for line in file:
        print(f"Строка: {line.rstrip()}")

Чтение по выбору
def read_file(filename, method='all'):
    with open(filename, 'r') as file:
        if method == 'all':
            return file.read()
        elif method == 'line':
            return [line.strip() for line in file]

print(read_file('C:/Users/anrey/Desktop/example.txt', 'all')) 
print(read_file('C:/Users/andrey/Desktop/example.txt', 'line')) 

2 ЗАДАНИЕ
def write_new_text():
    text = input("Введите текст для записи в файл (оставьте пустым, чтобы не менять файл): ")
    if text.strip() != "": 
        with open('user_input.txt', 'w', encoding='utf-8') as file:
            file.write(text)
        print("Текст записан в файл user_input.txt")
    else:
        print("Пустой ввод — файл не изменён.")
write_new_text()

# Если добавить запись
filename2 = 'user_input.txt'
text = input("Введите текст для добавления в файл(Добавится на следующей строке, старый текст сохраниться. Если ничего не хотите добавлять, то просто пропустите, нажав ENTER): ")
def append_text():
    with open(filename2, 'a', encoding='utf-8') as file:
        file.write('\n' + text)
    print("Текст добавлен в файл user_input.txt")
append_text()

3 ЗАДАНИЕ

def read_file_safe(filename, method='all'):
    try:
        if method == 'all':
            with open(filename, 'r') as file:
                content = file.read()
                print(content)
        elif method == 'line':
            with open(filename, 'r') as file:
                for line in file:
                    print(line.strip())
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден!")

read_file_safe('C:/Users/andrey/Desktop/example.txt','line')


ОБЪЕДИНЕНИЕ 2
method = input("Выберите метод (1 - запись нового файла, 2 - добавление текста): ")
text = input("Введите текст: ")
def (filename, method='all'):
if method == '1':
    with open('sema.txt', 'w') as f:
        f.write(text)
elif method == '2':
    with open('sema.txt', 'a') as f:
        f.write("\n" + text)



def write_to_file(filename, content, mod):
    if method == '1':
        with open(filename, 'w') as f:
            f.write(text)
    elif method == '2':
        with open(filename, 'a') as f:
            f.write("\n" + text)

method = input("Выберите метод (1 - запись нового файла, 2 - добавление текста): ")
text = input("Введите текст: ")
filename = 'sema.txt'
write_to_file(filename, text, method)
