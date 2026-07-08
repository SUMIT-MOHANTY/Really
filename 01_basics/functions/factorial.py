# def factorial (n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))


# fcatorial using loop
def factorial (n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

    
print(factorial(5))

# show me with an example iterate and tell me thsi loop hwo it works
# lets say 5 is the n then 
# result = 1
# for i in range(2, 5 + 1):
#     result *= i
#     print(f"i: {i}, result: {result}")


# why result is needed here
# result stores the cumulative product of the numbers from 2 to n, which is the factorial of n and it is set to 1 becasue multiplying
#  by 1 does not change the value of the product, and it serves as the identity element for multiplication.

