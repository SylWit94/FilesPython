try:
    file = open("./testFiles/fileToWrite.txt", mode='r')
    file.write('Hello jaktestowac.pl!')
except Exception as e:
    print(e)
    print(f'In block "except". Is file closed? {file.closed}')
finally:
    print(f'In block "finally". Is file closed? {file.closed}')
    file.close()
    print(f'In block "finally". Is file closed? {file.closed}')
    