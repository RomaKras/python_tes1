import json
from trio import open_file
#пример чтения файла
# file_data = open('data.txt','r')
# data = file_data.read()
# file_data.close()
# print(data)
# data = json.loads(data)
# print(data)
# print(data['Contry'])

class ReadAndPrintFile ():
    def __init__(self,file):
        self.file = file

    def ReadAndPrint(self):
        file_data = open(self.file,'r')
        #data = file_data.read()
        data = json.load(file_data)
        file_data.close()
        return data

data1 = ReadAndPrintFile('data.txt').ReadAndPrint()
print(data1['Contry'])
print(type(data1))