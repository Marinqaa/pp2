# Write a python program to convert snake case string to camel case string.
import re
def snake2camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


txt = str(input("Enter smth: "))
print(snake2camel(txt))

