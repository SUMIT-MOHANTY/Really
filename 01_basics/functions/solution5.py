# given its radius create a function that returs both the area and circumference of a circle
import math

def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

print(circle(5))
