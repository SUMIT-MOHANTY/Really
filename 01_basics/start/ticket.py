age  = 25
day2 = "Monday"
day = input("Please enter the day of the week: ")

price = 12 if age <= 12 else 20

if day == day2:
        price = price-2

print(f"Your ticket price is {price} dollars.")
