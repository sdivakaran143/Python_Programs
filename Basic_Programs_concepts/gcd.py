
def gcd(a,b):
    if a<b:
        c=a
    else:
        c=b

    while c!=0:
        if a%c==0 and b%c==0:
            print(f"\nGCD of {a} and {b} is {c}")
            val=c
            break
        c-=1
    return val    

def multy(c):
    x=lambda a,b=c:a*b
    for i in range(1,11):
        print(f"{i}x{c}={x(i)}")
#main function
a=int(input("enter a first value :"))
b=int(input("enter a second value :"))
c=gcd(a,b)
multy(c)

"""# swap
a=a+b
b=a-b
a=a-b
print(f"the values are swaped \n the value of \"a\" is {a} and  \"b\" is {b}")
"""