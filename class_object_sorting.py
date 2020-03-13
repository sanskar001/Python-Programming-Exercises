class employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return "({},{},{})".format(self.name,self.age,self.salary)
    
emp1 = employee("carl",37,70000)
emp2 = employee("sarah",24,60000)
emp3 = employee("Mark",40,40000)

employees = [emp1,emp2,emp3]

print(employees)

def emp_sorted(emp):
    return emp.salary

salary_sorted_employee = sorted(employees,key = emp_sorted)

print(salary_sorted_employee)