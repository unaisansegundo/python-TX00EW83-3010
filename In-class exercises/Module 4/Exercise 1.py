import random

guess = int(input('Guess a number from 1 to 100: '))
number = random.randint(1,100)

while guess != number:
    print(number) #Show the answer for debugging
    if guess > number:
        print('The number is too high')
        guess = int(input('Guess a new number: '))
    elif guess < number:
        print('The number is too low')
        guess = int(input('Guess a new number: '))
print('Good job you guessed the number!')
