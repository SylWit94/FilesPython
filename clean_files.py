import os

file_path_1 = os.path.join('testFiles', 'dataSets', 'dataSetBase.txt')
file_path_2 = os.path.join('testFiles', 'testDataSets', 'dataSet1.txt')
file_path_3 = os.path.join('testFiles', 'testDataSets', 'dataSet1copy.txt')
file_path_4 = os.path.join('testFiles', 'testDataSets', 'dataSet1copyRenamed.txt')
files = [file_path_1, file_path_2, file_path_3, file_path_4]

for file in files:
    if os.path.exists(file):
        os.remove(file)
    else:
        print('File to remove does not exist')
