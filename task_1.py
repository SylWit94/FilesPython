file = open("./testFiles/file_1.txt", mode='w')
file.write("That is my first file!")
file.close()
file = open("./testFiles/file_1.txt", mode='r')
print(file.read())
file.close()

