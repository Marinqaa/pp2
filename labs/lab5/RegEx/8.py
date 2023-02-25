# Write a Python program to split a string at uppercase letters.
import re
text = input("Enter a string: ")
print(re.findall('[A-Z][^A-Z]*', text))
