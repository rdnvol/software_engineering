import random
import math


def check_user_input(message):
    val = 0
    while True:
        try:
            val = int(input(message))
            break
        except ValueError:
            print('No.. input is not a number. It`s a string')
            continue
    return val


def task1():
    a = check_user_input('Print a: ')
    b = check_user_input('Print b: ')
    z = (math.cos(a) + math.cos(b)) ** 2 - (math.sin(a) - math.sin(b)) ** 2
    print(z)


def task2():
    while True:
        number = check_user_input('Print positive number: ')
        if number <= 0:
            print('Invalid input')
        else:
            break

    arr = []
    summa = 0
    for i in range(1, number - 1):
        if number % i == 0:
            arr.append(str(i))
            summa += i

    string = '+'.join(arr) + '=' + str(summa)
    if summa > number:
        print(f'''{number} is excessive number 
    {string}>{number}''')
    else:
        print(f'''{number} isn`t excessive number
        {string}<{number}''')


def task3():
    arr1 = random.sample(range(-10, 0), 5)
    arr2 = []
    summa = 0
    mean = 0
    for number in arr1:
        if number > 0:
            summa += number
            arr2.append(number)
    if len(arr2) > 0:
        mean = summa / len(arr2)

    print(arr1)
    min_element = min(arr1)
    if min_element >= 0:
        print('No negative elements')
    else:
        print(f'''Min negative element: '{min_element}' ''')
    print(f'''Mean: {mean}''')
    print(f'''Positive elements: {arr2}''')


task1()
task2()
task3()
