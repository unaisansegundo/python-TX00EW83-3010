cruise_type = input('Enter the cabin class of a cruise ship: ')

if cruise_type == 'LUX':
    print('Upper-deck cabin with a balcony')
elif cruise_type == 'A':
    print('Above the car deck, equipped with a window')
elif cruise_type == 'B':
    print('Windowless cabin above the car deck')
elif cruise_type == 'C':
    print('Windowless cabin below the car deck')
else:
    print('Invalid cabin class')