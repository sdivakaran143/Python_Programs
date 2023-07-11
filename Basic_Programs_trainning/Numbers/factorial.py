n=int(input("enter the value :"))
sum=1;
for i in range(n,0,-1):
    sum*=i
print(f"the factorial of {n} is {sum}")