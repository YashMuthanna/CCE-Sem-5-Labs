import os

file = open("sample1.txt", "r+")
chars = 0
lines = len(file.readlines()) #reads number of lines
file.seek(0) # sets pointer back to beginning of file
result = file.read()
words = 0
for i in result:
    chars=chars+1
    if(i == " " or i == "\n"):
        words = words+1

print("Number of words: ", words)
print("Number of lines: ", lines)
print("Number of characters: ", chars)
