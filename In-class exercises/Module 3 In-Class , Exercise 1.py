letter = input("Enter a letter: ")
vowels =  ["a" , "e" , "i" , "o" , "u"]

if letter in vowels:
    print("The letter entered is a vowel")
elif letter == 'y' :
    print("The letter y can sometimes be a vowel and other times a consonant")
else:
    print("The letter entered is not a vowel")

