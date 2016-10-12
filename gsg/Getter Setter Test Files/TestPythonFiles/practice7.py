#!/usr/bin/env python
#
# Program to read and print a file 
#
file = open("alice.txt","r")
text = file.readlines()
file.close()

text.reverse()

file = open("alice.txt","w")

x = 1

for line in text:
    line = str(x) + ". " + line
    file.write(line) # write lines to file
    x += 1

file.close()



