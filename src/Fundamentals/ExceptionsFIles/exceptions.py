
#Exception Handling
"""
Different exceptions are raised for different reasons. 
Common exceptions:
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly; 
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.

"""
num1 =7
num2 = 0
#print(num1/num2)

"""
To handle exceptions, and to call code when an exception occurs, you can use a try/except statement.
The try block contains code that might throw an exception. If that exception occurs, the code in the try block stops being executed, 
and the code in the except block is run. If no error occurs, the code in the except block doesn't run.

"""
try:
   num1 = 7
   num2 = 0
   print (num1 / num2)
   print("Done calculation")
except ZeroDivisionError:
   print("An error occurred")
   print("due to zero division")

   """
A try statement can have multiple different except blocks to handle different exceptions.
Multiple exceptions can also be put into a single except block using parentheses, to have the except block handle all of them.
   """
   try:
       variable =10
       print(variable + "hello")
       print(variable/2)
   except ZeroDivisionError:
       print("Divided by zero")
   except (ValueError,TypeError):
       print("Error Occurred")

"""
An except statement without any exception 
specified will catch all errors. These should be used sparingly, as they can catch unexpected errors and hide programming mistakes.
"""

try:
   word = "spam"
   print(word / 0)
except:
   print("An error occurred")

   #finally

   """
   To ensure some code runs no matter what errors occur, you can use a finally statement. The finally statement is placed at the bottom of a try/except statement. 
   Code within a finally statement always runs after execution of the code in the try, and possibly in the except, blocks.
   """
try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")

   """
   You can raise exceptions by using raise statement
   """

   print(1)
   #raise ValueError
   print(2)

   """
   In except blocks, the raise statement can be used without arguments to re-raise whatever exception occurred.
   """

#try:
   #num = 5 / 0
#except:
   #print("An error occurred")
  # raise

   #Assertions
   """
An assertion is a sanity-check that you can turn on or turn off when you have finished testing the program.
An expression is tested, and if the result comes up false, an exception is raised.
Assertions are carried out through use of the assert statement.
   """

   print(1)
   assert 2 + 2 == 4
   print(2)
   assert 1 + 1 == 3
   print(3)