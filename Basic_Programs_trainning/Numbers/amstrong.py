n=int(input("enter the value :"))
sum=0
m=str(n)

for i in m:
    sum+=int(i)**3
    print(int(i)**3)
if(n==sum):
    print("its a amstrong number")
else:
    print("its not an amstrong number")
