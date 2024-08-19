"""
print('Hello')

print('Hello, \n World!')

number = input('Write a number: ')

# Print the input number
print('Your number is: ' + number)



int_var = 3
float_var = 3.28
string_var = 'something'

print(type(int_var))
print(type(float_var))
print(type(string_var))

name = input('Name: ')
print(name)
name = name + ' cool'
print(name)


result = 10/8
print(result)
print(type(result))
rounded_result = int(result)
print(rounded_result)

"""
n1 = int(input('Write a number: '))
n2 = int(input('Write a number to add: '))
addition = n1 + n2
print('The result of the addition is: ' + str(addition))
print('The result of the addition is: ', addition)
print(f"The result of the addition is:  {addition}")

num = 1/3
print(num)
print(f"Rounded number is {num:.2f}")