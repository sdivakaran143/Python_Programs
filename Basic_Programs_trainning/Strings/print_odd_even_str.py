str=input("enter the string : ")
even=""
odd=""
for i in range(len(str)):
    if((i+1)%2==0):
        even+=str[i]
    else:
        odd+=str[i]
print(f"{odd}\n{even}")
