print('Hello World!')

star = 1
space = 7
while space > 1:
    print(' ' * space, '*' * star, ' ' * space)
    star += 2
    space -= 1

# name = input('What is your name? ')
name = 'andy'
print('Hello \'?\' ' + name)

# birth_year = input('Birth year: ')
birth_year = 1993
age = 2020 - int(birth_year)
print(age)

first = 'John'
last = 'Smith'
name = f'my name is {first} {last}'
print(name)

print(first.find('o'))
print(last.replace('Sm', 'What'))
print(first.title())

print(round(-2.6))
print(abs(-2.5))

import math
import random

print(math.ceil(2.5))
print(math.pi)

price = 1e6
good_credit = True
if good_credit:
    print('You need to put down ' + str(price * 0.1))
else:
    print('You need to put down ' + str(price * 0.2))

if len(name) < 3:
    print('name must be more than 3 characters')
elif len(name) > 50:
    print('can\'t be more than 50')
else:
    print('looks good !')

chance = 3
number = random.randint(1, 10)
myGuess = []
print('Guess a number, you have 3 chances')
while chance > 0:
    # guess = int(input('Guess: '))
    guess = random.randint(1, 10)

    repeat = True
    while repeat:
        if guess not in myGuess:
            repeat = False
            myGuess.append(guess)
        else:
            guess = random.randint(1, 10)

    print(f'Your guess {guess}')


    if number == guess:
        print('You win!')
        win = True
        break
    chance -= 1

else:
    print('Sorry you failed!')

exitGame = True
carStatus = ''
while not exitGame:
    command = input("> ").lower()

    if carStatus == command:
        if command == 'start':
            print('The car is already started')
        else:
            print('The car is already stopped')
        continue

    if command == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif command == 'start':
        print('Car started... Ready to go!')
        carStatus = command
    elif command == 'stop':
        print('Car stopped.')
        carStatus = command
    elif command == 'quit':
        exitGame = True
    else:
        print('Don\'t understand')

prices = [10, 20, 30]
total = 0
for i in prices:
    total += i
else:
    print(f'All items cost {total}')

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

numbers = [5, 2, 5, 2, 2]
for i in numbers:
    texts = ''
    for x in range(i):
        texts += 'X'
    print(texts)

numbers.insert(0, 2)
print(numbers.count(2))

numbers2 = numbers.copy()
numbers3 = []
for i in numbers2:
    if i not in numbers3:
        numbers3.append(i)
else:
    print(f'List : {numbers3}')

x, y, z = prices
print(f'{x}, {y}, {z}')

customer = {
    'name' : 'John',
    'age' : 30
}

print(customer.get('gender'))
print(customer.get('name'))
print(customer.get('birthdate', '1993'))


def convertNumber(inputNumbers):
    digits = [
        '🤓',
        '🙃',
        '🥺',
        '😫',
        '😁',
        '🤪',
        '😱',
        '😧',
        '🙄'
    ]

    my_number = ''
    for i in inputNumbers:
        my_number += f'{digits[int(i) - 1]} '
    else:
        return my_number


# inputNumbers = input('Numbers: ')
inputNumbers = '2321'
print(f'Your number is {convertNumber(inputNumbers)}')


def greet_user(my_name, age='12'):
    print(f'name: {my_name}, age: {age}')


greet_user(my_name="John", age="Wick")
greet_user("Smith")


def error_detect(prop):
    try:
        my_age = int(prop)
        print(my_age)
    except ZeroDivisionError:
        print('Age no 0')
    except ValueError:
        print('Inavlid value')


error_detect("asd")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point(10, 9)
point1.x = 10
print(point1.x)
point1.draw()


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hello I am {self.name}')


class Man(Person):
    def run(self):
        print('I am running')


a_man = Man('John')
a_man.talk()

import converters
# from converters import kg_to_lbs
# kg_to_lbs(100)

print(converters.kg_to_lbs(70))

from utils import find_max

numbers = [10, 3, 4, 6, 2]
maxNumber = find_max(numbers)
print(maxNumber)
print(max(numbers))

# package
# import ecommerce.shipping
from ecommerce.shipping import calc_shipping
from ecommerce import shipping

calc_shipping()
shipping.calc_shipping()

members = ["Andy", "Li", "Claire", "Helo"]
print(random.choice(members))


class Dice:
    def roll(self):
        print(f'({random.randint(1, 6)}, {random.randint(1, 6)})')


dice = Dice()
dice.roll()

from pathlib import Path

path = Path("ecommerce")
print(path)

path1 = Path("emails")
# print(path1.mkdir())
# print(path1.rmdir())

path2 = Path()
print(path2.glob('*.py'))
for file in path2.glob('*.py'):
    print(file)

for file in path2.glob('*'):
    print(file)

