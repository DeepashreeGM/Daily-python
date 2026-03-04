class Employee:
    company_name="DCL"
    def __init__(self):
        self.emp_name=None
        self.emp_sal=None
    def display_details(self):
        print("Empplyee Name:",self.emp_name)
        print("Employee Salary:",self.emp_sal)
        print("Conpanyname:", self.company_name)
    @classmethod
    def change_company_name(cls,new_company_name):
        cls.company_name=new_company_name
e1=Employee()
e1.emp_name="Deepa"
e1.emp_sal=80000
print("Before changing the company_name")
e1.display_details()
e1.change_company_name("Meta")
e1.display_details()