class Employee:
  def __init__(self, id, name, salary, dept):
    self.id = id
    self.name = name
    self.salary = salary
    self.dept = dept
    self.details = (id, name, salary, dept)

n = int(input("Enter number of employees: "))
l1 = []
for i in range(n):
  print("Enter id, name, salary, department: ")
  id, name, salary, dept = input().split()
  empObj = Employee(id,name,salary,dept)
  emp = Employee(id,name,salary,dept).details
  l1.append(emp)

x = input("enter ID to be searched: ")
flag = 0
for element in l1:
  if x == element[0]:
    print(f"Found\nName: {empObj.name}\nSalary: {empObj.salary}\nDepartment: {empObj.dept}")
    flag = 1

if flag == 0:
  print("Record Not Found")

