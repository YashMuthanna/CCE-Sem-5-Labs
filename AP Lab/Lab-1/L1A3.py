#Check if string is hexadecimal
s = input("Enter string: ")
flag = 0

for i in s:
    if ((i<'0' or i>'9') and (i<'A' or i>'F')):
        print("Not Hexadecimal")
        flag = 1
        break
if flag == 0:
    print("It is hexadecimal")

        
