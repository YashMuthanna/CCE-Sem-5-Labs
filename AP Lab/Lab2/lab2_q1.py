list1 = input("Enter string").split()
dict1 = {};
for word in list1:
    dict1[word] = list1.count(word)
print(dict1)

