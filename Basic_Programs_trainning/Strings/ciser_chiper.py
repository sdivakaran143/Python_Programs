str=input("enter the string :")
n=int(input("enter the key value : "))
cipertext=""
for i in range(len(str)):
    if ord(str[i])+n<=ord('z'):
        cipertext+=chr(ord(str[i])+n)
    else:
        m=(ord(str[i])+n)-ord('z')
        cipertext+=chr(ord('a')+(m-1))
print("the cipher text was ",cipertext)