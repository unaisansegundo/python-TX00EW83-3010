import random
random_4 = random.randint(1,6)

def random_3():
    return str(random.randint(0,9))

def random_4():
    return str(random.randint(1,6))

digit3 = random_3() + random_3() + random_3()
digit4 = random_4() + random_4() + random_4() + random_4()
print(f'3-digit code: {digit3}')
print(f'4-digit code: {digit4}')