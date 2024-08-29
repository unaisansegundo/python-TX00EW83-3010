gender = input("Enter your gender: ")
hemoglobin = float(input("Enter your hemoglobin value (g/l): "))

if gender == "Female":
    if hemoglobin < 117:
        print('Your hemoglobin value is below the normal for adult females')
    elif hemoglobin > 155:
        print('Your hemoglobin value is above the normal for adult females')
    elif 117 <= hemoglobin <= 155:
        print('Your hemoglobin value is normal for adult females')
elif gender == "Male":
    if hemoglobin < 134:
        print('Your hemoglobin value is below the normal for adult males')
    elif hemoglobin > 167:
        print('Your hemoglobin value is above the normal for adult males')
    elif 134 <= hemoglobin <= 167:
        print('Your hemoglobin value is normal for adult males')