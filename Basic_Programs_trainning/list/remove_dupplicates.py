n=int(input("enter the value :"))
list=[]
for i in range(n):
    list.append(int(input(f"enter value li1 {i+1} : ")))
for i in range(n-1):
    for j in range(i+1,n):
        if(list[i]==list[j]):
            list[j]="null"
i=0
while(i<len(list)):
    if list[i]=="null":
        i=-1
        list.remove("null")
    i+=1
print(list)