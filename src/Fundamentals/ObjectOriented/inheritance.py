# Inheritance

"""
Inheritance provides a way to share functionality between classes. 
Imagine several classes, Cat, Dog, Rabbit and so on. Although they may differ in some ways (only Dog might have the method bark), they are likely to be similar in others (all having the attributes color and name). 
This similarity can be expressed by making them all inherit from a superclass Animal, which contains the shared functionality. 
To inherit a class from another class, put the superclass name in parentheses after the class 
"""
class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr")

class Dog(Animal):
    def bark(self):
        print("Woof")

fido = Dog("Fido","Blue")
print(fido.name)
fido.bark()


"""
A class that inherits from another class is called a subclass.
A class that is inherited from is called a superclass.
If a class inherits from another with the same attributes or methods, it overrides them.
"""



"""
Inheritance can also be indirect. One class can inherit from another,
 and that class can inherit from a third class. 
"""
class Aa:
    def method(self):
        print("A method")
    
class B(Aa):
    def another_method(self):
        print("B method")
    
class C(B):
    def third_method(self):
        print("C method")
    
c = C()
c.method()
c.another_method()
c.third_method()

"""
The function super is a useful inheritance-related function that refers to the parent class. 
It can be used to find the method with a certain name in an object's superclass.
"""
class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()
            
B().spam()