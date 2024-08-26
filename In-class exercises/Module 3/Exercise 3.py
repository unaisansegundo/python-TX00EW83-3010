""""
i = 1
while i < 11:
    print(i)
    i = i+1
"""
"""
greetings = int(input('How many times do you want to greet?'))
first_greeting = 0
while first_greeting < greetings:
    print('Good morning!')
    first_greeting += 1
"""

"""
command = input('Enter a command:')
while command != "STOP":
    print('Running command!')
    command = input('Enter a command:')
print("The program stops now")
"""
"""
import random
dice1 = dice2 = roll_times = 0
while dice1 !=6 or dice2 !=6:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    roll_times += 1
    print(f'Dice1 : {dice1}\nDice2 : {dice2}')
print (f'The dice was rolled {roll_times} to get both on 6')
"""
"""
command = input('Enter a command:')
while command != "STOP":
    if command == "BREAK":
        break
    print('The command is running...' + command)
    command = input('Enter a command:')
print('Stopping program...')
"""

"""
num = 10
while num < 100:
    num = num + 10
    if num == 50:
        continue
    print("Current number: ", num)
"""
"""
command = input('Enter a command:')
while command != "STOP":
    if command == "BREAK":
        break
    print('The command is running...' + command)
    command = input('Enter a command:')
else:
    print('Goodbye')
print('Stopping program...')
"""

first_num = 1
while first_num <= 5:
        second_num = 1
        while second_num <= 5:
            print(f'{first_num} times {second_num} is {first_num*second_num}')
            second_num += 1
        first_num += 1

