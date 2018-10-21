#for i in range(10):
 #   if not i%2 == 0:
  #      print(i+1)

def my_func():
    print("The result is " + str(1))

def max(x,y):
    if x > y:
        return x
    else:
        return y
#print(max(5,6))

# docstrings

def shout(word):
    """
    print a word with an 
    exclamation mark
    """
    print(word + "!")

shout("spam")

def add(x,y):
    return x+y

def do_twice(func,x,y):
    return func(func(x,y),func(x,y))
a=5
b=10

print(add,a,b)

#######################################333
#modules
#The basic way to use a module is to add
#  import module_name at the top of your code,
#  and then using module_name.var to access 
# functions and values with the name var in 
# the module.

import random
for i in range(5):
    value= random.randint(1,6)
    print(value)


from math import pi
print(pi)

# Types of modules
# custom modules written by self
# custom modules from external sources
# preinstalled modules
# 

def print_nums(x):
    for i in range(x):
        print(i)
        return

print_nums(10)

def func(x):
    res = 0
    for i in range(x):
        res += i
    return res
print(func(4))

