n = int(input("enter number of rows in matrix: " ))
m = int(input("Enter number of columns in matrix: "))


print("Enter values of matrix 1")

dict1 = {}
dict2 = {}

for i in range(n):
    for j in range(m):
        x = int(input())
        t = (i,j)
        dict1[t] = x
for i in range(n):
    for j in range(m):
        x = int(input())
        t = (i,j)
        dict2[t] = x

for i in range(n):
    for j in range(m):
        x = dict1[(i,j)] + dict2[(i,j)]
        print(x, end=" ")
    print("\n")
