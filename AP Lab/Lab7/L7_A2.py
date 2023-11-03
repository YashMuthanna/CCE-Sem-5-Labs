def extsort(file_list):
    sorted_files = sorted(file_list, key = lambda x: x.split('.')[-1])
    print(sorted_files)

file_list = []
n = int(input("Enter the number of files: "))
for i in range(n):
    fstr = input("Enter File Name: ")
    file_list.append(fstr)
    
extsort(file_list)
