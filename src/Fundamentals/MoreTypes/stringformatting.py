#string formatting
"""
String formatting provides a more powerful way to embed non-strings within strings.
 String formatting uses a string's format method to substitute a number of arguments in the string.
"""
nums = [4,5,6]
msg = "Numbers:{0}{1}{2}".format(nums[0],nums[1],nums[2])
print(msg)

#string formatting can also be done with named arguments
a ="{x},{y}".format(x=5,y=9)
print(a)


