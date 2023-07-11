str1=input("enter the str1 :")
str2=input("enter the str2 :")
str2cpy=str2
output=""
for i in str1:
    if i in str2:
        output+=i
        str2=str2.replace(i,"")
print(f"the common characters in \"{str1}\" and \"{str2cpy}\" is \"{output}\"")