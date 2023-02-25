# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
txt = str(input())
x = re.search('[A-Z]+[a-z]+$', txt)
if x:
    print("Match found!")
else:
    print("No match found.")
