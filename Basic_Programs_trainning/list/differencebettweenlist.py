import sys
n=int(input("enter the value :"))
list=[]
list2=[]
s=0
s1=0
for i in range(n):
    list.append(int(input(f"enter value li1 {i+1} : ")))
    s+=list[i]
for i in range(n):
    list2.append(int(input(f"enter value li2 {i+1} : ")))
    s1+=list2[i]
    list2[i]=list[i]-list2[i]

print(f"the difference of two list is {list2}")
print(f"the sum difference of two list is {s-s1}")
