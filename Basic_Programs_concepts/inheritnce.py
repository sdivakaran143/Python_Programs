#inheritance 
class person:
    fees=6000
    def __init__(self,name,age,yob):
        self.name=name
        self.age=age
        self.yob=yob
    
    def det(self):
        detial=f"NAME: {self.name}\nAGE: {self.age}\nYOB: {self.yob}"
        return detial
    
    def ag(self):
       age=2021-self.yob
       return age

class students(person):
    def __init__(self,name,age,yob,fees):
        super().__init__(name, age, yob)
        self.fees=fees

class mech(students):
    
    def __init__(self, name, age, yob, fees, dept):
        super().__init__(name, age, yob, fees)
        self.dept=dept
    def det(self):
        detial=f"NAME: {self.name}\nAGE: {self.age}\nYOB: {self.yob}\nFEES: {self.fees}\nDEPT: {self.dept}"
        return detial   

class staff(person):
    def __init__(self, name, age, yob,salary):
        super().__init__(name, age, yob)
        self.salary=salary

    def det(self):
        detial=f"NAME: {self.name}\nAGE: {self.age}\nYOB: {self.yob}\nSALARY: {self.salary}"
        return detial   



s1=students("divakaran", 18, 2003,70000)
m1=mech("mecheshwaran", 20, 2000, 55000,"mechanical")
st1=staff("muthukumaran", 40, 1984,52000)
print(s1.det(),"\n")
print(m1.det(),"\n")
print(st1.det(),"\n")

