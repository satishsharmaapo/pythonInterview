class Employee:
    '''doc string(Description)'''
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def info(self):
        print('*'*30)
        print('Employee Number:',self.eno)
        print('Employee Name:',self.ename)
        print('Employee Salary:',self.esal)
        print('Employee Address:',self.eaddr)
        print('*'*30)

e1=Employee(100,'Satish',100000,'Hyderabad')
e2=Employee(200,'Rakesh',100000,'Bhilai')
e1.info()
e2.info()
print(e1.__doc__)
help(e1)

# .....................self variable is same as this object in java
# self is a reference variable which is always pointing to current Object......


class Student:
    def __init__(self):
        print(id(self))
s=Student()
print(id(s))