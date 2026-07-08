# create a function that accept any number of key arguments and print them in the form of key and value
def print_key_value(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(print_key_value(name="Alice", age=30, city="New York"))