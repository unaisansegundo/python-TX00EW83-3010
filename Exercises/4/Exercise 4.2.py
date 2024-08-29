while True:
    inches = float(input("Enter a number in inches: "))
    if inches <= 0:
        break
    print(f'{inches}in equals to {inches * 2.54}cm')
