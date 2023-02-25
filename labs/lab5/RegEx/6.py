# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

txt = str(input("Enter a string: "))
x = re.sub('[ ,.]', ":", txt)
print(x)
