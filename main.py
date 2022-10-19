num_1 = float(input('Введите первое число: '))

operation = input('''
Введите арифметическое действие:
+ сложение
- вычитание
* умножение
/ деление
** Возведение в степень
''')
num_2 = float(input('Введите второе число: '))


def calculate():
    if operation == '+':
        print(f' {num_1} + {num_2} = {num_1 + num_2}')
    elif operation == "-":
        print(f' {num_1} - {num_2} = {num_1 - num_2}')
    elif operation == '*':
        print(f' {num_1} * {num_2} = {num_1 * num_2}')
    elif operation == '/':
        print(f' {num_1} / {num_2} = {num_1 / num_2}')
    elif operation == '**':
        print(f' {num_1} ** {num_2} = {num_1 ** num_2}')
    else:
        print('не правильное действие ')


calculate()
