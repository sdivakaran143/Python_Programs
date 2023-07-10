
def tables(v):
    x=lambda a,b=v : a*b
    for i in range(1,11):
        print(i,"X",v,"=",x(i))

person={
    "key1":"car",
    "key2":"bike",
    "key3":"boat"
}
li=["new1","new2","new3","new4","new5","new6","new7"]

def name(n):
    print("Welcome to python dear "+n)