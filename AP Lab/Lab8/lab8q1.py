import re

for i in dir(re): #dir() prints all the functions in the module
    if "find" in i:
        print(i)


