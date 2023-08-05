import os

# dir_full_path = os.path.join("testFiles", "newTestFiles")
dir_full_path = os.path.join("testFiles", "invalid", "newTestFiles")
# print(f'New directory will be created in: "{os.getcwd()}"')
# print(f'New directory path: "{dir_full_path}"')

if not os.path.exists(dir_full_path):
    os.makedirs(dir_full_path, exist_ok=True)
else:
    print("Directories already exist")
    