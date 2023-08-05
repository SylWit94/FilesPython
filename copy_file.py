import shutil
import os

file_path = os.path.join('testFiles', 'fileToCopy.txt')
dir_for_copy_file = os.path.join('testFiles', 'invalidPath')
new_file_path = os.path.join(dir_for_copy_file, 'copiedFile.txt')

if os.path.exists(file_path):
    if os.path.exists(dir_for_copy_file):
        shutil.copy(file_path, new_file_path)
    else:
        print('Directory for file to copy does not exist')
else:
    print('File to copy does not exist')
