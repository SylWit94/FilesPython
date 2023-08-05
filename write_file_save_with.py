try:
    with open("./testFiles/fileToWriteWith.txt", mode='r') as file:
        file.write('Hello!!!')
except Exception as e:
    print(f'Exception: {e}')
finally:
    print(f'In block "finally". Is file closed? {file.closed}')
    