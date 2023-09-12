import os

file = open("sample1.txt", "r")
res= file.read().split()

dict = {}
for i in res:
    if i not in dict.keys():
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)
