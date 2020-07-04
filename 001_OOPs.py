# Object Oriented Programming (OOPs):
# ....................................

# java and python both have oops concepts have internal changes
# internal implementation are different ........

# .............
# class ,object , reference variable
# class is the template
# it is blueprint 
# Object is instance of class 
# ...................

# eg1: Building 1000F
# .....................
# Architect ===> Plan 
# once the plan is ready based on that we can construct buiding
# all the things in plan

# Any no of building based on plan
# mumbai ,pune etc....
# 200 villas or community have the same plan....
# KCR ===> double bedroom appartments....
# 5 lakhs all flat based on same class...

# plan act as a blueprint or template of buildings...
# plan is nothing but class

# once class is ready the buildings constructed based on the plan ===> objects
# The physical existence of a class is nothing but object...

# n no of buildings is constructed by the means of plan...
# Once class is ready ====> multiple objects ...
# eg2: Sony High end xyz model==> 10 lakhs
# take the model information
# another shop
# sony High end xyz model==>9.5 lakhs

# in another state ==>10.6 lakhs

# i selected sony end model of cost ==>9.5 lakhs

# we get the model of same.
# it is beacause of same model.
# almost on state have same model have same features .

# Plan/Design is nothing but class .
# Each physical TV ===> Objects.

# based on Same Mold/Dye we can create n number of buckets with the same size.
# mold/dye==>class 
# buket==> Object

# class ==> blueprint/template/mold/dye/design/plan for objects.
# Object is physical existence of a class.
# Physical instance of a class.


# .....................
# class    object===> one to many

# Object   reference ==> one to one | one to many.

# ....................................

class Student:
    ''' This Class developed by Satish for Demo Purpose''' 
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    
    def talk(self):
        print("Hello My Name is :",self.name)
        print("My Rollno is : ",self.rollno)

# for this class we can create any no of objects
s=Student(100,'Sunny')
print(s.name)
print(s.rollno)
s.talk()

s1=Student(200,'Bunny')
s1.talk()

s2=Student(300,'Chinny')
s2.talk()
print(__doctype__)
# 3 object and 3 reference variable here