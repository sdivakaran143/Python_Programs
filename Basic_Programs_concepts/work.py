# file handling 
import os

fn=str(input("Enter file name :"))

def output():
        f=open(fn,"r")
        print(f.read())

def menu():
    print("1 to write\n2 to append\n 3 to read\n4 to delete")
    option=int(input("enter your choice :"))
    return option
e=0
while e!=1:
    op=menu()
    c=0
    if op==1:
        type="w"
    elif op==2:
        type="a"
    elif op==3:
        output()
        c=1
    elif op==4:
        c=1
        os.remove(fn)
        break

    if os.path.exists(fn):
        if c==0:
            f=open(fn,type)
    else:
        f=open(fn,"x")
    if c==0:
        w=str(input("write the content to insert in file:\n"))
        f.write(w)
        f.close()
        print("file sucessfully closed")
    e=int(input("enter 1 to end (OR) press any key to continue :"))
    

