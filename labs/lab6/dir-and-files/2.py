# Write a Python program to check for access
# to a specified path. Test the existence, readability,
# writability and executability of the specified path
import os
print('Exist:', os.access('C:\\Users\\nurma\\Downloads\\pp2\\labs\\lab5\\row.txt', os.F_OK))
print('Readable:', os.access(
    'C:\\Users\\nurma\\Downloads\\pp2\\labs\\lab5\\row.txt', os.R_OK))
print('Writable:', os.access(
    'C:\\Users\\nurma\\Downloads\\pp2\\labs\\lab5\\row.txt', os.W_OK))
print('Executable:', os.access(
    'C:\\Users\\nurma\\Downloads\\pp2\\labs\\lab5\\row.txt', os.X_OK))
