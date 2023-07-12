k=input("enter the String : ")
file=open("F:/Python_Programs/Basic_Programs_trainning/basic File I&O operations/file.txt")
str=file.read()
count=0
for i in str.split():
    if k==i:
        count+=1
print(f"the key count is {count}")