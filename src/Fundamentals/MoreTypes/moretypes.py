"""
The None object is used to represent the absence of a value. 
It is similar to null in other programming languages. 
Like other "empty" values, such as 0, [] and the empty string, it is False when converted to a Boolean variable. 
When entered at the Python console, it is displayed as the empty string.
"""

#The None object is returned by any function that doesn't explicitly return anything else.
def greeter():
    print("Hello")

#greet = greeter()
#print(greet)


# DICTIONARIES
"""
Dictionaries are data structures used to map arbitrary keys to values. 
Lists can be thought of as dictionaries with integer keys within a certain range.
Dictionaries can be indexed in the same way as lists, using square brackets containing keys.
"""
ages = {"Dave":2,"Sam":3,"John":4}
#print(ages["Sam"])

"""
 Only immutable objects can be used as keys to dictionaries.
 Immutable objects are those that can't be changed. 
 So far, the only mutable objects you've come across are lists and dictionaries. 
 Trying to use a mutable object as a dictionary key causes a TypeError.
"""

"""
Just like lists, dictionary keys can be assigned to different values.
However, unlike lists, a new dictionary key can also be assigned a value, not just ones that already exist.
"""
squares = {1: 1, 2: 4, 3: "error", 4: 16, }
squares[8] = 64
squares[3] = 9
#print(squares)

#To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.
nums = {1:"one",2:"two"}
#print(1 in nums)

#print(nums.get(1))

pairs = {
        3: "apple",
         "orange": [2, 3, 4],
         True: False,
         None: "True",
         }

print(pairs.get("orange"))
print(pairs.get(1))
print(pairs.get("asdf", "not in dictionary"))

## TUPLES
"""
Tuples are very similar to lists, except that they are immutable (they cannot be changed). 
Also, they are created using parentheses, rather than square brackets.
"""
words = ("ad","ds","ds")

print(words[0])

#Like lists and dictionaries, tuples can be nested within each other.


# list
list =["one", "two"]


# dictionary
dict ={  1: "one", 2: "two" }


# tuple
tp =("one", "two")

#Tuples can be created without the parentheses, by just separating the values with commas.
my_tuple = "one", "two", "three"
print(my_tuple[0])


#An empty tuple is created using an empty parenthesis pair.
tpl = ()
