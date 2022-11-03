#python function

def add(a,b):
    c=a+b
    return c
    
a=10#int(input("enter the value for A :"))
b=20#int(input("enter the value for B :"))
c=add(a,b)
print("sum of the ",a," and ",b," is ",c)

print("\n")
def fname(name):
    print("welcome to python Mr."+name)
fname("Divakaran")
fname("ranjith")
fname("suresh")
print("\n")

#Arbitrary Arguments, *args
def fname(*name):#tuple 
    print("welcome to python Mr.",name[0])
fname("Divakaran","diva")

#Keyword Arguments
def fnam(child1, child2,child3):
    print("the youger child is "+child2)
fnam(child1="diva",child2="dharsan",child3="divan")

#Arbitrary Keyword Arguments, **kwargs
def fnam(**child):
    print("the youger child is "+child["child3"])
fnam(child1="diva",child2="dhar",child3="divan")

print("\n")
#default parameter value 
def para(pname="python"):
    print("welome to "+pname)

para("c++")
para("c")
para("java")
para()#it shows default value python 
print("\n")

#list in a function 
def lis(list1):
    for i in list1:
        print(i)
    list1[2]="keerthi"

list1=["divakaran","diavan","guru"]
lis(list1)
print(list1)

# return function
def ret(x):
    return x*5*2
print("the value of x*5*2 it returns",ret(5))        

#pass

#recursion 
def rec(x):
    if 0<x:
        v=x+rec(x-1)
    else:
        v=0 
    return v

print(rec(100))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#lambda function
"""v=int(input("which table you need to display :"))
x=lambda a,b=v : a*b
for i in range(1,100):
    if i==11:
        break
    print(i,"X",v,"=",x(i))"""

def lam(x):
    return lambda a:a*x
TRP=lam(3)
print(TRP(32))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------