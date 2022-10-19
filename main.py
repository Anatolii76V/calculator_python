num_1 = float(input('Введите первое число: '))
operation = input('''Введите арифметическое действие: + ,- ,* ,/ ,** : ''')
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
calc_again = input('Хотите продолжить нажмите Y если нет то N ')


def again():
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()
