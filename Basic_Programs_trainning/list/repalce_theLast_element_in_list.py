n=int(input("enter the value :"))
list=[]
for i in range(n):
    list.append(int(input(f"enter value {i+1} : ")))
list2=[]

for i in range(n):
    list2.append(int(input(f"enter value {i+1} : ")))

for i in range(n):
    if i==0:
        list.pop()
    list.append(list2[i])
print(list)