from envparse import env
import os
from casino_logic import bet
env.read_envfile('settings.env')
balance = int(os.getenv('MY_MONEY'))

while True:
    command = input('Хотите сыграть еще?')
    if command == 'нет':
        print(f'На вашем балансе {balance}')
        break
    elif command == 'да':
        rate = int(input('Введите число для ставки'))
        amount = int(input('Введите сумму для ставки '))
        if rate < 1 or rate > 30:
            print('Неправильное число для ставки')
            continue
        if amount > balance:
            print('Неправильная сумма для ставки')
            continue
        balance = bet(rate, amount, balance)

