# Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
txt = str(input("Enter smth: "))
x = re.findall('[a-z]+_[a-z]+', txt)
print(x)
if x:
    print("Match found! ")
else:
    print("None")
