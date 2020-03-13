# This is python program to understand the oops concepts.

class person:
    def __init__(self,p_name="Tina",p_age=23,p_gender="female"):
        self.p_name = p_name
        self.p_age = p_age
        self.p_gender = p_gender
    
    def getp_name(self):
        return self.p_name 
    
    def getp_age(self):
        return self.p_age 

    def getp_gender(self):
        return self.p_gender
    
    def person_info(self):
        print("This is  person information.")


class employee():
    def __init__(self,other,e_salary=40000):
        # other.__init__()
        # super().__init__()
        self.e_name = other.p_name
        self.e_age = other.p_age
        self.e_gender = other.p_gender
        self.e_salary = e_salary
    
    def gete_name(self):
        return self.e_name  
    
    def gete_age(self):
        return self.e_age
     
    def gete_gender(self):
        return self.e_gender
    
    def gete_salary(self):
        return self.e_salary
    
    def employee_info(self):
        print("This is employee information")

   
person1 = person("ritik",22,"male")
person2 = person("sanskar",19,"male")

employee1 = employee(person2,90000)
print(employee1.gete_name())
print(employee1.gete_age())
print(employee1.gete_gender())
print(employee1.gete_salary())