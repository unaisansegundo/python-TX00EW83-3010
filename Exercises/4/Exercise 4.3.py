n_list = []
while True:
    input_n = input("Enter a number to add to the list: ")
    if input_n == '':
        break
    n_list.append(int(input_n))

print(f'The smallest value in the list is {min(n_list)} and the biggest is {max(n_list)}')