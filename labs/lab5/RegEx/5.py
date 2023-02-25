# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
txt = str(input())
x = re.search('a.*b$', txt)
if x:
    print("Match found!")
else:
    print("No match found.")
    