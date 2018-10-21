#Write a Python program which accepts the radius of a circle
#  from the user and compute the area.

from math import pi

print("Welcome to the Area Generator")
radius = float(input("Enter the radius"))
area = str(pi* radius**2)
print("Area = " + area)
