str=input("Enter the string :")
print('a'<'b')
i=0
while(i<len(str)-1):
    if str[i]>str[i+1]:
        temp=str[i]
        str=str[:i]+str[i+1]+str[i+1:]
        str=str[:i+1]+temp+str[i+2:]
        i=-1
    i=i+1 
print(str)
reverse=""
for i in str:
    reverse=i+reverse
print(reverse)