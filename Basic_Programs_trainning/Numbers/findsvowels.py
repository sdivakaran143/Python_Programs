str=input("enter the String :")
count=0
for i in str:
    if  i in "aeiou" :
        count+=1;
print(f"There are {count} Vowels in the Word") 
