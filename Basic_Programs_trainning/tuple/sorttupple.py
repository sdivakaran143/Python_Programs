tuple=(1,5,6,7,4,2,1,4,6,8,5,3,2,1,2,3,4,8,9,0,6,9)
tuplist=list(tuple)
tuplist.sort()
tuple=list(tuplist)
print(tuple)
for i in range(-1,-len(tuple),-1):
    print(tuple[i],end=" ")
print()
for i in range(0,len(tuple),):
    print(tuple[i],end=" ")
