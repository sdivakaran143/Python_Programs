n=int(input("enter the number : "))
factotrs=[]
evensum=0
oddsum=0
for i in range(n,0,-1):
    if n%i==0:
        factotrs.append(i)
        if i%2==0:
            evensum+=i
        else:
            oddsum+=i
print(factotrs)
print(f"higest factor is {max(factotrs)}\nevenfactor sum is {evensum}\noddfactor sum is {oddsum} ")