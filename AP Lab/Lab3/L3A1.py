def counter(string1):
    upper = 0
    lower = 0
    for i in string1:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
    print("Upper case: ", upper)
    print("Lower case: ", lower)
string1 = "The quick BroWn fox"
counter(string1)
