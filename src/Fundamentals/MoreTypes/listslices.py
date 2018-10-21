"""
List slices provide a more advanced way of retrieving values from a list. Basic list slicing involves indexing a list with two colon-separated integers. 
This returns a new list containing all the values in the old list between the indices.
"""
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])


#Like the arguments to range, the first index provided in a slice is included in the result, but the second isn't.

"""
If the first number in a slice is omitted, it is taken to be the start of the list.
If the second number is omitted, it is taken to be the end.
"""
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:9])
print(squares[7:])

"""
List slices can also have a third number, representing the step, to include only alternate values in the slice.
"""
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

"""
Negative values can be used in list slicing (and normal list indexing). When negative values are used for the first and second values in a slice (or a normal index), they count from the end of the list
"""
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))
