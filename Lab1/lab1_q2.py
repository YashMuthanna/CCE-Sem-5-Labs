curr = 1
n = 6
for i in range(n):
    for j in range(i+1):
        print(curr, end=" ")
        curr+=1
    print("\n", end="")
