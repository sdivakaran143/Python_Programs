import sys
n=int(input("enter the value :"))
list=[]
s=sys.maxsize
l=-sys.maxsize
for i in range(n):
    list.append(int(input(f"enter value {i+1} : ")))
    s=list[i] if s>list[i] else s
    l=list[i] if s<list[i] else l
print(list)
print(f"the smallest:{s} and largest:{l}")
