n=int(input("enter the value :"))
list=[]
sum=0
mul=1
for i in range(n):
    list.append(int(input(f"enter value {i+1} : ")))
    sum+=list[i]
    mul*=list[i]
print(list)
print(f"the sum:{sum} and product:{mul}")
