number = int(input('Input a number to get its factorial: '))

if number <= 0:
    print('Thank and bye!')
else:
    n = result = 1
    while n < number:
        n += 1
        result = result * n
        print(result) #Debug
    print(f'The factorial of the number {number} is {result}')
