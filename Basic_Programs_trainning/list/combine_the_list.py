n=int(input("enter the value :"))
list=[]
output=""
for i in range(n):
    list.append(int(input(f"enter value li1 {i+1} : ")))
    output+=str(list[i])
print(f"output -> {output}")