# Write a Python program to test whether a given path
# exists or not. If the path exist find the filename
# and directory portion of the given path.
import os
print("Test a path exists or not:")
path = r'c:\\pp2\\Lab5\\row.txt'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))