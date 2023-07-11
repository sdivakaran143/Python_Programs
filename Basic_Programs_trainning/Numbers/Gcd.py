a=int(input("enter the value 1: "))
b=int(input("enter the value 2: "))
c= a if a<b else b
for i in range(c,0,-1):
    if a%i==0 and b%i==0:
        print(f"the GCD of {a} and {b} is {i}")
        break
print(f"the difference between {a} and {b} is {abs(a-b)} ")