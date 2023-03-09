# Write a Python program
# to copy the contents of a file to another file
from shutil import copyfile
copyfile('C.txt', 'D.txt')

# Write a Python program to delete file by specified path.
# Before deleting check for access and whether a given path exists or not.
import os

if os.path.exists('C:\\Users\\nurma\\Downloads\\pp2\\labs\\lab6\\dir-and-files\\textfile.txt'):
    os.remove('C:\\Users\\nurma\\Downloads\\pp2\\labs\\lab6\\dir-and-files\\textfile.txt')
else:
    print("Such file does not exist!")