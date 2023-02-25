# Write a Python program to convert a given camel case string to snake case.
import re
def camel2snake(txt):
    x = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', txt)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', x).lower()

txt = str(input("Enter a string: "))
print(camel2snake(txt))
