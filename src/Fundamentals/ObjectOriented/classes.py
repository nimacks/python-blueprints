"""
Objects are created using classes, which are actually the focal point of OOP.
The class describes what the object will be, but is separate from the object itself. In other words, a class can be described as an object's blueprint, description, or definition.
You can use the same class as a blueprint for creating multiple different objects. 

Classes are created using the keyword class and an indented block, which contains class methods (which are functions). 
"""

class Cat:
    def __init__(self,color,legs):
        self.color = color
        self.legs = legs


felix = Cat("ginger",4)
rover = Cat("Dog-colored",5)

"""
Classes are created using the keyword class and an indented block, 
which contains class methods (which are functions). 

All methods must have self as their first parameter, although it isn't explicitly passed, 
Python adds the self argument to the list for you; you do not need to include it when you call the methods. 
Within a method definition, self refers to the instance calling the method.
"""

# Methods
"""
Classes can have other methods defined to add functionality to them. 
Remember, that all methods must have self as their first parameter.
These methods are accessed using the same dot syntax as attributes. 
"""

class Dog:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")

fido = Dog("Fido", "Brown")
print(fido.name)
fido.bark()

# Class attributes

"""
Classes can also have class attributes, created by assigning variables within the body of the class. 
These can be accessed either from instances of the class, or the class itself.
"""
""" class Dogs:
    legs=4
    def __init__(self,name,color):
        self.name = name
        self.color = color

fido = Dog("Fido","Yellow")
print(fido.legs)
print(fido.name) """