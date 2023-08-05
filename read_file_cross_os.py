import os

# path = "./testFiles/fileToRead.txt"
path = os.path.join('testFiles', 'fileToRead.txt')
file = open(path)
print(file.read())
print(path)
