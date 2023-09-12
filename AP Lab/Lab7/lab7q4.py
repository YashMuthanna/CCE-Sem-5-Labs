import os
import re

valid = open("valid.txt", "w")
invalid = open("invalid.txt", "w")
n = int(input("Enter number of email IDs: "))

for i in range(n):
    x = input("enter email: ")
    if re.match(".+@.+\..+", x):
        valid.write(x)
    else:
        invalid.write(x)
