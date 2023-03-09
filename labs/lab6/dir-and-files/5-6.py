# Write a Python program to write a list to a file.
fruits = ['apple', 'cherry', 'banana']
with open('a.txt', 'a') as a:
    for i in fruits:
        a.write("\n")
        a.write(i)
text = open('a.txt')
print(text.read())

# Write a Python program to generate 26 text files
# named A.txt, B.txt, and so on up to Z.txt
import string
for letter in string.ascii_uppercase:
    with open(letter + ".txt", "w") as f:
        f.write(letter)

