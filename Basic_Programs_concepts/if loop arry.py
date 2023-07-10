#PHYTHON WORKOUTS 2
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#if else
a=10
b=30
c=7
#if #if-else #elif #and
if a>b and a>c:print("\"a\" is grater than \"b\" and \"c\"") #shot hand if 
elif b>a and b>c:
    print("\"b\" is grater than \"a\" and \"c\"")
else:
    print("\"c\" is grater than \"a\" and \"b\"")

#shot hand if else
print("a is greter then b")if a>b else print("b is greater than a")
a=b
print("a is greter then b")if a>b else print("A and B are equal") if a==b else print("b is greater than a")#shot hand if else with three condition 

#or
if a==b or a>b:
    print("a is greater than b or equal to b\n")
a=10

#nested if 
if a<b:
    print("a is smaller than b")
    if a>c:
        print("a is greater than c")
        if a==b:
            print("a is equal to b")
        else:
            print("a is not equal to b")
else:
    print("a is greater than b")        

#pass statement 
if a<b:
    pass # having an empty if statement like this, would raise an error without the pass statement
# having an empty if statement like this, would raise an error without the pass statement
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#while loop
i=1
#while  break statement
while i<=10:
    print("break",i)
    if i==5:
        break #it terminates a whole loop
    i+=1
i=1 
print("\n")

#continue statement
while i<=10:
    if i==5:
        i+=1 
        continue  #it terminates a single loop
    print("continue ",i)
    i+=1
else:
    print("while is loop ended")
print("\n")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#for loop
list1=["apple","mango","juice","raw fruit","slice"]

for i in list1:#loop with list
     print(i)

for i in "divakaran":#loop throught the string
    print(i)
print("\n")

#break statement
for i in list1:
    #print(i) print("\n")
    if i=="juice":
        break    
    print(i) #it not prints after break 
print("\n")

#continue statement 
for i in list1:
    #print(i) #it prints before continue # it does not skips raw fruit
    if i=="raw fruit":
        continue 
    print(i) #it not prints after continue # it skips raw fruit
 
 # range() 

for i in range(10): 
    print(i) 
print("\n")   
for i in range(5,10):# with start value 
    print(i)
print("\n")   
for i in range(2,10,3):# with start value  and increment value 
    print(i)
else:
    print("for loop finished")    

#nested for loop 
for i in range(1,6):
    for j in range(1,6):
        print(i,",",j)
    print("\n") 
#pass
for i in range(1,10):
    pass            
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#array (list)
"""arr=list()
ar=0
for i in range(5):
    x=int(input("enter the value :"))
    ar+=x
    arr.append(x)
print(ar)
print(arr)"""
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
