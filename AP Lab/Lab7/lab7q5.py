import re
x = input("Enter string to be checked: ")
if re.match(r'^(.).*\1$', x):
    print("Satisfies")
else:
    print("Does not satisfy")
