#text analyser
"""
This is an example project, showing a program that analyzes a sample file to find what percentage of the text each character occupies.
This section shows how a file could be open and read.
"""

#functions

#This part of the program shows a function that counts how many times a character occurs in a string.
def count_char(text,char):
    count = 0
    for c in text:
        if c == char:
            count+=1
    return count

filename = input("Enter a filename: ")

with open(filename) as f:
   text = f.read()

print(count_char(text,"t"))

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))