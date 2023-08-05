with open("./testFiles/file_2.txt", mode='w') as file:
    file.write("This is my second file!")

with open("./testFiles/file_2.txt", mode='r') as file:
    print(file.read())
    