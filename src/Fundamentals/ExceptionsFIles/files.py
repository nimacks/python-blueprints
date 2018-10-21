#Files
"""
You can use Python to read and write the contents of files.
Text files are the easiest to manipulate. Before a file can be edited, it must be opened, using the open function.
"""
myfile = open("c:\\test.txt")
myfile.close()

"""
You can specify the mode used to open a file by applying a second argument to the open function.
Sending "r" means open in read mode, which is the default. 
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.

Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).

# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")
"""

#reading files
#The contents of a file that has been opened in text mode can be read using the read method.

myfile = open("C:\\test.txt","r")
contents = myfile.read()
print(contents)
myfile.close()

"""

To read only a certain amount of a file, you can provide a number as an argument to the read function. This determines the number of bytes that should be read. 
You can make more calls to read on the same file object to read more of the file byte by byte. With no argument, read returns the rest of the file
file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()
"""

"""
To retrieve each line in a file, you can use the readlines method to return a list in which each element is a line in the file.
"""
myfile = open("C:\\test.txt","r")
contents = myfile.readlines()
print(contents)
myfile.close()

#you can use a for loop to iterater through the lins in the file
myfile = open("C:\\test.txt","r")

for line in myfile:
    print(line)

myfile.close()

#writing to files
#To write to files you use the write method, which writes a string to the file.
myfile = open("test.txt","w")
myfile.write("This file has been written to")
myfile.close()

myfile = open("test.txt","r")
print(myfile.read())
myfile.close()

#The write method returns the number of bytes written to a file, if successful.


#When a file is opened in write mode, the file's existing content is deleted.


#The write method returns the number of bytes written to a file, if successful.
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()
"""
An alternative way of doing this is using with statements.
 This creates a temporary variable (often called f), which is only accessible in the indented block of the with statement.
"""

with open("filename.txt") as f:
   print(f.read())