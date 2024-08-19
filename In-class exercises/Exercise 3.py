n_cafe = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input('What is the price of a typical student lunch? '))
groceries = float(input('How much money do you spend on groceries in a week? '))
print('Average food expenditure: ')
weekly = (n_cafe * price) + groceries
daily = weekly / 7
print(f'Daily: {daily} euros')
print(f'Weekly: {weekly} euros')