from random import choice


def bet(rate, amount, balance):
    numbers = [range(1, 31)]
    number = choice(numbers)
    if number == rate:
        print("Вы выиграли")
        return balance + rate
    else:
        print('Вы проиграли!')
        return balance - rate
