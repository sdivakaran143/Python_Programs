#scop[e]

#local scope # function inside the function 
def hai():
    x=100
    def hello():
        print("from hello ",x)
    print("from hai ",x)
    hello()
    return x

print(hai())

#global scope
x=108 
def new():
    print("global scope ",x)

new()

#naming variables
x=1532
def name():
    x=1000
    print("local ",x)

name()
print("global",x)


#global key word 
x=1564

def globa():
    global x 
    print(x)
    x=1        #changes are occures in global x 

globa()
print(x) #we can see the changes