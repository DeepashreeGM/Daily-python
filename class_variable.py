class Employee:
    CompanyName="DCL" #class_Variable
    def __init__(self):
        self.Emp_Name=None #Instance_variable
        self.Emp_id=None #Instance_variable
e1=Employee()#Object_Creation
e1.Emp_Name="Deepashree GM"
e1.Emp_id="DCL01"
print(e1.Emp_Name)
print(e1.Emp_id)
print(e1.CompanyName) #invoking class variable using obj_reference
print(Employee.CompanyName) #invoking class variable using class 
e2=Employee()#Object_Creation
e2.Emp_Name="Pallavi GM"
e2.Emp_id="DCL02"
print(e2.Emp_Name)
print(e2.Emp_id)
print(e2.CompanyName) #invoking class variable using obj_reference
print(Employee.CompanyName) #invoking class variable using class 



