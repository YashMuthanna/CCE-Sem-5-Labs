n = int(input("Enter number: "))
temp = n
sum1 = 0
while n>0:
    x = n%10
    sum1 += x*x*x
    n = n//10
if temp == sum1:
    print("It is armstrong number")
else:
    print("It is not armstrong number")
