# Write a Python program to insert spaces between words starting with capital letters.
import re
text = input("Enter a string: ")
x = re.sub(r"(\w)([A-Z])", r"\1 \2", text)

print(x)
