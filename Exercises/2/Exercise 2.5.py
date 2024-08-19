from math import remainder

talents = float(input('Enter talents:'))
pounds = float(input('Enter pounds:'))
lots = float(input('Enter lots:'))

total_weight_gr = (((((talents * 20) + pounds) * 32) + lots) * 13.3)

total_weight_kg = total_weight_gr / 1000
remainder_gr = (total_weight_gr - int(total_weight_kg) * 1000)
print(f"{int(total_weight_kg)} kilograms and {remainder_gr:.2f} grams.")