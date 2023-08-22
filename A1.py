import math
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
flag = True
for i in range(n,m):
    for j in range(2,i):
        if (i%j) == 0:
            flag = False
            break
    else:
        print(i)
