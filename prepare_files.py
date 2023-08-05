import os
import shutil

new_dir = os.path.join('testFiles', 'testDataSets')
file_to_copy_path = os.path.join('testFiles', 'dataSets', 'dataSetBase.txt')
new_file_path = os.path.join('testFiles', 'testDataSets', 'dataSet1.txt')
the_newest_file_path = os.path.join('testFiles', 'testDataSets', 'dataSet1copy.txt')
renamed_file_path = os.path.join('testFiles', 'testDataSets', 'dataSet1copyRenamed.txt')

if not os.path.exists(new_dir):
    os.makedirs(new_dir, exist_ok=True)
else:
    print('Directory already exist')


shutil.copy(file_to_copy_path, new_file_path)
shutil.copy(new_file_path, the_newest_file_path)

if os.path.exists(the_newest_file_path):
    if not os.path.exists(renamed_file_path):
        os.rename(the_newest_file_path, renamed_file_path)
    else:
        print('The name already exists')
else:
    print('Old file already exists')
    