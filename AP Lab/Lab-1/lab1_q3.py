n = int(input("Enter number of strings: "))
list1 = []
count=0
for i in range(n):
    x = input("Enter string: ")
    list1.append(x)
    if x[0] == x[-1] and len(x)>=2:
        count = count+1
print("Count: " ,fdi count)
for i in list1:
    if len(i)%2 != 0:
       print(i)





