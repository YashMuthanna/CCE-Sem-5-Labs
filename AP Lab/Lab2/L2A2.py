list1 = list(map(int, input("Enter list 1").strip().split()))
list2 = list(map(int, input("Enter list 2").strip().split()))

union = list1+list2
diff = [i for i in list1 if i not in list2]
intersection = [i for i in list1 if i in list2]

print("Union is: ", union)
print("Difference is: (List1 - List2) ", diff)
print("Intersection is: ", intersection)
