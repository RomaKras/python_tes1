import json
from tkinter.font import names

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


# user_location=input()
# user_time=input()
# print("Current location is "+ user_location + " and time is " + user_time)


a = input()
b = input()
if str.isdigit(a) and str.isdigit(b) :
    while  c := input():
        v = True if int(c) in range(int(a), int(b)) else False
        if v == False :
          break
    print(v)
a = input()
list_list = []
max_list = []

for i in range(int(a)):
    lista = input().strip()
    max_list.append(max(lista))

max_list=sorted(max_list,reverse=True)
print(';'.join( max_list))


