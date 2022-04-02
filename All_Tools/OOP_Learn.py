#Learn OOP

class Employee:
    num_employee = 0
    def __init__(self,firstname,lastname) :
        self.firstname=firstname
        self.lastname=lastname
        Employee.num_employee += 1
    @property
    def full_Name(self):
        return self.firstname +','+self.lastname
    @full_Name.setter
    def full_Name(self,name):
        first,last=name.split(' ')
        self.firstname=first
        self.lastname=last
        

    @staticmethod
    def is_work_day(day):
        if day ==5 or day ==6:
            return False
        return True    
    

class Developer(Employee):
    def __init__(self, firstname, lastname,prog_lang):
        super().__init__(firstname, lastname)
        self.prog_lang=prog_lang
print(Employee.num_employee)
employee_1=Employee('Mahmoud','Elkot')
employee_2=Employee('Test','User')
dev_1=Developer('elkout','mahmoud','python')
print(dev_1.full_Name)
dev_1.full_Name='asfmg,nwretl ejrhfweguewnv'
print(dev_1.full_Name)
print(int.__add__(1,2))
""" print(Employee.num_employee)
print(employee_1.num_employee)
Employee.num_employee=5
print(Employee.num_employee)
employee_1.num_employee=10
print(Employee.num_employee)
     """
""" print(Employee.is_work_day(3))
print(employee_1.is_work_day(3))
#print(Employee.is_work_day(3))
print(help(employee_1))
 """
#print(Employee.num_employee)



""" employee_1.FirstName='Mahmoud'
employee_1.lastName='elkot'
employee_2.FirstName='User'
employee_2.lastName='Test' """
""" print(employee_1.firstname)
print(employee_1.lastname)
print(employee_2.firstname)
print(employee_2.lastname)
 """
#print(employee_1.full_Name())

#employee_1.






