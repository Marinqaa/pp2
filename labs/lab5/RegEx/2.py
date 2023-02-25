# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re

txt = input("Enter a string: ")
x = re.search('ab{2,3}', txt)
if x:
    print("Match found! ")
else:
    print("None")
