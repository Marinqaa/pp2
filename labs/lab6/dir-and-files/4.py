# Write a Python program to count the number
# of lines in a text file.

def file_length(fname):
    with open(fname, 'r') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print("Number of lines in the file: ", file_length('C:\\Users\\nurma\\Downloads\\pp2\\labs\\lab6\\lol.txt'))