age = int(input("please enter your age:"))

if age < 13:
    print("You are a Child.")
elif age < 20:
    print("you are a Teenager.")
elif age < 60:
    print("You are an Adult.")
else:
    print("You are a Senior Citizen.")