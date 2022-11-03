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