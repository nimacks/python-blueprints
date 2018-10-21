#List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.
#For example, we can do the following:
# a list comprehension
cubes = [i**3 for i in range(5)]

print(cubes)

#A list comprehension can also contain an if statement to enforce a condition on values in the list.

evens = [i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)
