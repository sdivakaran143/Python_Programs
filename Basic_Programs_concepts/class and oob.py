#class and object 

class Student:
    def __init__(self,name,rollno,Yob):#we can also can use (var,name,rollno,Yob) for self 
        self.name=name
        self.rollno=rollno
        self.Yob=Yob
    def det(self):
        detial=f"NAME: {self.name}\nREGNO: {self.rollno}\nYOB: {self.Yob}"
        return detial
    def age(self):
        age=2021-self.Yob
        return age

"""name=str(input("enter the name : "))
rollno=int(input("enter the register no:"))
Yob=int(input("enter yor birth year:"))
print("\n")
s1=Student(name,rollno,Yob)"""

s1=Student("Divakaran",2013021,2003)

print(s1.det())
print("AGE: ",s1.age())

#pass
class person:
    pass

#delete 
#del s1
#print(s1.name)

#del s1.name
#print(s1.name)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#class and object +inheritanec
import datetime as dt
x=dt.datetime.now()
y=int(x.strftime("%Y"))

class student:
    fees=15000
    def __init__(self,name,std,yob):
        self.name=name
        self.yob=yob
        self.std=std 
    def age(self):
        return y-self.yob
    def det(self):
        detial=f"NAME: {self.name}\nSTD: Year {self.std}\nYOB: {self.yob}\nFEES: {self.fees}\nAGE:{self.age()}"
        return detial

class mech(student):
    fees=65000
    def __init__(self, name, std, yob,dept):
        super().__init__(name, std, yob)
        self.dept=dept




s1=student("divakaran",2,2003)
m1=mech("ram",1, 2002, "mech")
print(m1.det())
print("\n")
print(s1.det())
print(mech.__mro__)