text = input("Write a text (Max 255 char): ")
happy = ":-)"
sad = ":-("

happy_times = text.count(':-)')
sad_times = text.count(':-(')

if happy_times > sad_times:
    print('Happy')
elif happy_times < sad_times:
    print('Sad')
elif happy_times == 0 and sad_times == 0:
    print('Nothing')
elif happy_times == sad_times:
    print('Unsure')
