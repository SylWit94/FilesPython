import os

file_path = os.path.join('testFiles', 'fileToRemove.txt')

if os.path.exists(file_path):
    os.remove(file_path)
else:
    print('File to remove does not exist')
