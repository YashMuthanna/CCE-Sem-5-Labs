import os

file = open("sample1.txt", "r")
res = file.readlines()
res = res[::-1]
for i in res:
    print(i)
