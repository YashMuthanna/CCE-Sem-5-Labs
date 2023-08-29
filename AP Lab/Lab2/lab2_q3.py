import random

dict1 = {}
n = int(input("Enter number of elements: "))
dict2 = {}
sum1 = 0
datatype= "number"
for i in range(n):
    val1 = input("Enter value: ")
    y = random.randrange(0,100)
    if val1.isnumeric() and datatype == "number":
        val1 = int(val1)
        sum1 = sum1 + val1
    else:
        datatype = "string"
    dict2[y] = val1
        

if datatype == "number":
    print("Average: ", sum1/len(dict2))
elif datatype == "string":
    str = ""
    for i in dict2.values():
        str += i
    print("Concatenated string: " + str)
    val = input("Value to be searched ")

    for i in dict2:
        if(dict2[i] == val):
            print("Value found at: ", i)
    print("Displaying strings with ONLY special characters: ")

    for i in dict2:
        flag = 0
        for c in dict2[i]:
            if c.isalnum() == True:
                flag = 1
                continue;
        if flag == 0:
            print(dict2[i])
    
