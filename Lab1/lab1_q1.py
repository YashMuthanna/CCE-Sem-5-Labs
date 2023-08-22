n = int(input("Enter the size of the list1 "))
print("\n")
list1 = list(int(num) for num in input("Enter the list items separated by space ").strip().split())[:n]

m = int(input("Enter size of list2 "))
print("\n")
list2 = list(int(num) for num in input("Enter list items separated by space ").strip().split())[:m]

list3=[]
for i in range(n):
    if list1[i]%2 != 0:
        list3.append(list1[i])
for i in range(m):
    if list2[i]%2 == 0:
        list3.append(list2[i])

print(list3)
