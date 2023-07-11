str =input("enter the string : ")
for i in str :
    if not(i.isalpha() or i.isdigit()):
        str=str.replace(i,"")
print("the altered string is ",str)