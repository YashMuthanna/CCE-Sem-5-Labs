class Employee:
    def __init__(self,id,name,salary,department):
        self.id = int(id)
        self.name = name
        self.salary = int(salary)
        self.department = department

    def __del__(self):
        print(f"Employee {self.id} has been deleted")

    def displayDetails(self):
        print("Employee Details:")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

temp_emp_id = 2912
emp_list = []
n = int(input("Enter the number of employees: "))
for i in range(n):
    name = input("Enter the name: ")
    salary = int(input("Enter the salary: "))
    department = input("Enter the department: ")
    employ = Employee(temp_emp_id,name,salary,department)
    emp_list.append(employ)
    temp_emp_id+=1

for i in range(n):
    emp_list[i].displayDetails()
