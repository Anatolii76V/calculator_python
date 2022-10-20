def restart():
    choice = input('Хотите продолжить нажмите Y если нет то N ')
    if choice.upper() == 'Y':
        calculate()
    elif choice.upper() == 'N':
        print('До свидание.')
    else:
        restart()


def calculate():
    num_1 = float(input('Введите первое число: '))
    operation = input('''Введите арифметическое действие: + ,- ,* ,/ ,** : ''')
    num_2 = float(input('Введите второе число: '))

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
    restart()


calculate()
