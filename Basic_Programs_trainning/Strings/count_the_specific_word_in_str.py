str=list(input("enter the string : "))
key=input("enter the word to find : ")
count=0
for i in str:
    if i==key:
        count+=1
print(f"the word {key} appered {count} times ")