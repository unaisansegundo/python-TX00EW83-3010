length = float(input('What is the length of the zander in cm:'))
limit = float(42)

if length < limit:
    print(f'The zander is {limit-length} cm too small, release it')
else:
    print('The zander meets the size requirement')