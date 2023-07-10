
#python workouts  

print("Enter a year to find leap year or not leap year:")#diaplaying 
"""year=float(input("enter a year:"))  #inputing 
print(type(year))   #to know tha data type 
print(year,"is leap year")  #double quoat 
print(year,'is non leap year')  #single quoat """
a,A=10,20 #single line assing 

print("\nthe value of a is ",a,"the value of A is",A,"\n")# python is case senstive

#example for  varisbles cases
variable2=A
variable_3=a 
_varable=A
print("variable2,variable_3,_varable",variable2,variable_3,_varable)

myCamelCase='camel'
MyPascalCase='pascal'
my_snake_case='snake' 
print("\ncamel case = ",myCamelCase,"\npascal case = ",MyPascalCase,"\nsnake case = ",my_snake_case)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#adding two varriable(char)
var1='diva'
var2='karan'
var3=var1+var2
print(var3)
#adding two varriable(int)
var1=50
var2=50
var3=var1+var2
print(var3)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#defining the global variable
x='awsome'
def myfunc():
  global x
  x="fantastic"

myfunc()

print("\nPython is " + x,"\n")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

x=57j          #complex data type example  colex must come with "j"
print(type(x)) # displaying  the data type 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import random  # example for random using random module(random.randrange(0,100)) 
print("\nThe random number between 0 to 100 is ",random.randrange(100))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#multi line string 
stng='''\nLike many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.However,
Python does not have a character data type, a single character is simply a string with a length of 1.Square brackets can be used to access elements of the string.\n'''
print(stng)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#for loop by using string every atring is an array 
for x in "divakaran":
  print(x)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#to find the sring length we are using len()
print("\nlength of the strting 'stng' ",len(stng))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#To check if a certain phrase or character is present in a string   #in and not in 
check="bharath ghaneasan is my classmate"
#in 
print("\nA word classmate is available in string :","classmate" in check)
print("A word classmate is available in string :","classa" in check)

if "bharath" in check:
    print("\nA word bharth is  available in string ")
else:
    print("\nA word bharth is not available in string ")  

#not in 
print("\nA word classmate is not  available in string :","classmate"not in check)
print("A word classmate is not available in string :","classa"not in check)

if "barath"not in check:
    print("\nA word bharth is not available in string \n")
else:
    print("\nA word bharth is available in string\n ")  
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# string slicing 
slce="divakaran"
print(slce[:-4])#negative index value 
print(slce[5:])#positive index value  value 
print(slce[0:4])#positive index value  value 

# uppercase lowercase
print("\nupper case :",slce.upper())
print("lower case :",slce.lower())

#remove white space   #strip
a = "   Hello , World!    "
print(a.strip()) # returns "Hello, World!"

#replace string 
print("strings are replaced  a to k : ",slce.replace("a", "k"))

#split  # srings was splited where ever  "," in the string
print("strings are splitted ",a.split(","))

#string concordinating 
n1='python'
n2='programing'

print(n1+n2)#without space
print(n1+" "+n2) #withspace

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#sring formate # Use the format() method to insert numbers into strings
name="\niam divakaran my age is {}+ "
age=18
print(name.format(age)) 
print("my age is {} ".format(age))

#type1
myod="\ni ordered {} mango ,It cost was {}rs, I paid the bill {}rs"
mango=18
cost=200.58
bill=250
print(myod.format(mango,cost,bill))

#type2
myod="i ordered {0} mango ,I paid the bill {2}rs ,It cost was {1}rs\n "
print(myod.format(mango,cost,bill))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#format() more methods 
frmt="my name divakaran my bank balance is {:<8} rupees "#Left aligns the result (within the available space)
print(frmt.format(100))
frmt="my name divakaran my bank balance is {:>8} rupees "#Right aligns the result (within the available space)
print(frmt.format(100))
frmt="my name divakaran my bank balance is {:^8} rupees "#Center aligns the result (within the available space)
print(frmt.format(100))
frmt="my name divakaran my bank balance is {:=8} rupees "#Places the sign to the left most position
print(frmt.format(-100))
frmt="my name divakaran my bank balance is {:,} rupees "#Use a comma as a thousand separator
print(frmt.format(10000000))
frmt="my name divakaran my bank balance is {:.2f} rupees "#Use to display as a float value 
print(frmt.format(1001))

frmt="the binary value of 502 is {:b}"# used to display the binary value 
value=502
print(frmt.format(value))
frmt="the octal value of 502 is {:o}"# used to display the binary value 
value=502
print(frmt.format(value))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#escape character 
print("my name is \"divakaran\" its shows in double quotes\n")#new line and double quoutes 
print("example \t for \ttab\'\\t\'") #example for tab and back slash

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#deletng a variable 
del age
#print(age)  i comment this becas it shows error we deleted the variable age 
# NameError: name 'age' is not defined
print('\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# string modify string And string METHOD

str="Welcome to our modify string And string METHOD"
st="divakaran"
print(str.upper())
print(str.lower())
print(str.capitalize()) #its captize the first word 
print(str.casefold()) #its similoar to lower()
print(st. center(20,"."))#taking up the space of 20 characters, with "divakaran" in the middle:
print(str.count("string")) # it shows how many times a word occupies in the string 
print(st.count("a",2,8))# 22 is start value 37 is end value it search between position 2 to 8
print(str.find("And"))
print("swapcase :",st.swapcase())
print("isupper :",st.isupper())
print("islower :",st.islower())
st="1234"
print("isdigit :",st.isdigit())
print("isnumeric :",st.isnumeric())
print("isalphanumeric :","asd143".isalnum())
print("isalpha :","abcd".isalpha())
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# isinstance( buit in function which return bool value  and check the data type 
isin=10  #in intger
print("\nits is integer data type  :",isinstance(isin,int))
print("its is float data type :",isinstance(isin,float))
isin=1j #in complex
print("its is complex data type :",isinstance(isin,complex))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

list1=[10,"divakaran",143,1]
print(list1)
print(list1[0:4])
print(list1+2*list1)
list1[1]="sdivakaran"
print(list1)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#list constructure
list2=list(("name1","twooo",2,3j,"new","peeople",12,3))  # note the double round brackets 
print("\nindex value 1 in list2 is :",list2[1])
print("\nnegative index value -1 in list2 is :",list2[-1])
print("\nrange of index in list  is :",list2[1:3])

list2[1:4]=["one",2,"three"] #RANGE OF ITERMS  CHANGED 1 TO 3 
print(list2)

print("length of list2 is :",len(list2))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#to check the list by if condition 
if "one" in list2:
  print("\nthe word  one is  in the list2\n")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#list3 created       
list3=["one",2,"five"]   
print("list3 is ",list3)

list3[1:2]=["two",3,"four",5] #replaicing a range of value and inserting a value 
print("After replacing and inserting the value in List 3   ",list3) 

list3[1:5]=[2]  #replaicing a range of value and deleting  some  value 
print("After replacing and deleteting the value in List 3   ",list3,"\n") 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#add list iterms     

print("\n\n add list iterms \n")
list4=list(("one",2,"three"))
alp=["a","b","c","d","E"]

list4.append("four")  #append in the list it append at the end of the list
print("\nsucessfullly appended :",list4)

list4.insert(4,"five")  #to insert in the list at specified position  
print("\nsucessfullly inserted :",list4)

list4.extend(alp) #To extend/append elements from another list to the current list, use the extend() method.
print("\nsucessfullly extened :",list4)

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
tpl=("mango","apple") #tuple 
list4.extend(tpl)
print("\nsucessfullly extened list with tuple  :",list4,"\n")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#remove list iterms 

list4.remove("one")
print("\nsucessfullly removed the specific iterm :",list4,"\n")

list4.pop(0)
print("\nsucessfullly pop the specific iterm by index :",list4,"\n")

#If you do not specify the index, the pop() method removes the last item.
list4.pop()
print("\nsucessfullly pop the last iterm without index :",list4,"\n")

del list4[0]
print("\nsucessfullly delete the 0 (index value) iterm :",list4,"\n")

#The del keyword can also delete the list completely. 
del list3  #deleted list3

#The clear() method empties the list. The list still remains, but it has no content.
# the del key word deletes  a variable but the clear()method only deletes the content of the valriable  
list4.clear()
print("the content of the list4 are cleared ",list4)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#loop in the list 

list5=["apple","mango","jackfuit","pineapple","watermelon","water botel"]
i=0

#for loop
for x in list5:
  print(i," iterm is ",x)
  i+=1
print("\n")
i=0
for x in range(len(list5)):
  print("by range ",i," of ",list5[x])
  i+=1
print("\n")

#while loop
i=0
while i<len(list5):
  print(i," while of list is ",list5[i])
  i+=1
print("\n")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#loop by List Comprehension
[print("by loop comprehension ",x) for x in list5]


list6=["apple","mango","grapes","gova","cherry"]

list1=[x for x in list6 if 'a' in x] #for + in check
print("\n",list1)

list1=[x for x in list6 if "a" not in x] # for + not in check
print("\n",list1)

list1=[x for x in list6 if "apple"!=x ] #for + if !=
print("\n",list1)

list1=[x for x in list6] #for loop
print("\n",list1)

list1=[x for x in range(10)] #for in range 
print("\n",list1)

list1=[x for x in range(10) if x<5] # for in range + if conditon 
print("\n",list1)

list1=[x.upper() for x in list6] # upper + for 
print("\n",list1)

list1=["repeat" for x in list6] #  for  with  custom word 
print("\n",list1)

list1=[ x if x!="apple"  else "rose milk" for x in list6 ] # if else in for loop
print("\n",list1,"\n")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#we can assing a list items into variable 
a,b,c,d,e=list6
print(a)
print(b)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#sort list 
print("\nsort list\n")
list6.extend(list6)
list7=list((11,21,53,64,5,7,8,9,11,1,2))
print("\n ascending ")
list6.sort()# it sort ascending by default 
print(list6)

list7.sort()
print(list7)
print("\n decending ")
list6.sort(reverse=True)#sort by decending 
print(list6)

list7.sort(reverse=True)
print(list7)

"""list6[:5]=["Mango","Apple","Grapes","rose"]  #we changes some items in capital letter 
print(list6)

list6.sort()#resulting in all capital letters being sorted before lower case letters:
print(list6)

list6=['Apple', 'Grapes', 'Mango', 'apple', 'apple', 'cherry', 'cherry', 'gova', 'rose']     # it output without cccase sensitibvity 
list6.sort(key=str.lower)
print(list6)"""

list6.reverse()# it reverse thr list in reverse # the list already in decending order so it shows in acendinhg order
print(list6)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#copy list
list8=list6   #You cannot copy a list simply by typing list8 = list6, because: list8 will only be a reference to list6, 
print(list8)   #and changes made in list6 will automatically also be made in list8.
list8[:5]=["friuts"]
print("list6",list6)

#its a correct way to copy the list
list8=list6.copy()
print(list8)

list8[:5]=["apple"]
print("\nlist6",list6) # now its not  affect a list 6 we copied a list 6 to 8 

print("\n")
list8=list(list5)
print(list8)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#join list

# "+" method 
list9=list8+list7
print("\nsucessfully joined the two list\n",list9)

#append() method 
for x in list8:
  list9.append(x)
print(list9)

print("the length of list9 is",len(list9))

#extend method 
list9.extend(list6)
print("\nlist9 is ",list9)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#unpacking list
l=["apple","berry","carrot"]
red,blue,orange=l
print(red)
print(blue)
print(orange)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#tuple 
print("\ntuple")
tuple1=tuple(("apple","bamboo","carrot"))  # note the double round-brackets 3 CONSTRUCTUR
print(type(tuple1))
print("before changing inn tuple :",tuple1)

#NOTE:::You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# adding a item in a tuple 
list1=list(tuple1)
list1[0]="orange"
tuple1=tuple(list1)
print("after changing in tuple :",tuple1)

# adding a item in a tuple by using append()
list1=list(tuple1)
list1.append("apple")
tuple1=tuple(list1)
print(tuple1)

#adding two tuples 
tuple2=("water","juice","soda","wine")
tuple1+=tuple2
print("\"two tuples are added\"",tuple1)

tuple1=('orange', 'bamboo', 'carrot', 'apple', 'water', 'juice', 'soda', 'wine')

#deletying the iterm in tuple 
list1=list(tuple1)
list1.remove("orange")
list1.remove("carrot")
list1.remove("water")
list1.pop(1)
tuple1=tuple(list1)
print("\"some iterm are removed\"",tuple1)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#unpacking tuple
(red,yellow,white,dred)=tuple1
print(red)
print(yellow)
print(white)
print(dred)

print("\n*Asteris")#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
(red,yellow,*others)=tuple1
print(red)
print(yellow)
print(others)
print("\n*Asteris middle")
(red,*middle,yellow)=tuple1
print(red)
print(middle)
print(yellow)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#loop throught tuple
print("\nloop throught tuple\n")
#for loop
for x in tuple1:
  print(x)

print("\nloop throught tuple by range len\n")
for i in range(len(tuple1)):
  print(tuple1[i])

#while loop
print("\nloop throught while loop\n")
i=0
while i<len(tuple1):
  print(tuple1[i])
  i+=1
 #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 #join tuples
tuple3=tuple2+tuple1
print(tuple3) 

#mulityply the tuples 
tuple3=tuple2*2
print(tuple3)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
tuple3=(00,6,1,52,13,4,5,6,6,87,7,98,2,22)
x=tuple3.index(6)# it shows is index value
print("index of 6 is :",x)
x=tuple3.count(6)#it counts how many times 6 occurs 
print("count of 6 is :",x)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#python set 
print("\nSET\n")
set1={"amazon","flipkart","snapdeal"}
#or we can 
#set1=set(("amazon","flipkart","snapdeal","mythra","amazon"))
print(set1)
print("\n for loop in set ")
for x in set1:
  print(x)
#adding a iterm in a set by add()
set1.add("mythra")
print("\"MYTHRA ADDED SUCESSFULLY\"",set1)
#adding a set in a another set 
set2=set(("swigy","ubereats","zomatoo"))
set1.update(set2)
print("updated sucessfully",set1)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#remove set
#remove  
set1.remove("flipkart") #if the iterm does not exist it shows an error
print("flipkart removed",set1)
#discard
set1.discard("amazon")#if the iterm does not exist it does not shows an error
print(set1)

#pop()
#you can also use the pop() method to remove an item, but this method will remove the last item.
#Remember that sets are unordered, so you will not know what item that gets removed.
x=set1.pop()
print(x,"is poped")
print(set1)
#clear() methopd emties the set
set1.clear()
print(set1)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#python loop set
for x in set2:
  print(x)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# join sets
#union()
set1={"flipkart","amazon","mythra"}
set3=set1.union(set2)
print(set3)
#update
set1.update(set2)
print(set1)
set2.add("flyereats")
print(set2)
#intersection update 
set1.intersection_update(set2)#its update in existring llist
print(set1)
x=set1.intersection(set2)#it update in new list
print(x)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#DICTONARY 

dict1={
  "a":"apple",
  "b":"bannana",
  "c":1998
}
print(len(dict1))
print(type(dict1))
#acess dict
x=dict1["a"]
print(x)
#get()
x=dict1.get("b")
print(x)
print("\n")
#get keys 
print(dict1.keys())
x=dict1.keys()
print("before : ",x)
dict1["d"]="donkey"
print("after : ",x)
print("\n")
#get values
x=dict1.values()
print("before",x)
dict1["e"]=1878
print("after : ",x)
print("\n")
#iterms()
x=dict1.items()
print("before : ",x)
dict1["e"]=2003
print("after : ",x)
print("\n")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#change iterms 
#adding iteams 
dict1.update({"e":2020})
print("change iterms : ",x)

dict1.update({"year":2021})
print("change iterms : ",x)
print("\n")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#remove iterms 
#pop()
dict1.pop("a") #it removes "a" key
print("after pop : ",x)
print("\n")
#popiterm()
dict1.popitem() #it removes a last key that inserted 
print("after popiterm : ",x)
print("\n")
#del
del dict1["b"]
print("after del b : ",x)
print("\n")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#loop dict

for i in dict1:
  print(i)
  
print("\nkeys")
for i in dict1.keys():
  print(i)

print("\nvalues")
for i in dict1.values():
  print(i)

print("\niterms")
for i in dict1.items():
  print(i)

print("\niterms")
for i,y in dict1.items():
  print(i,y)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#copy dict 
#copy
dict2=dict1.copy()
print("dict2 copy() : ",dict2)

dict2.clear()# i clear this dict2

#dict()
dict2=dict(dict1)
print("dict2 dict() : ",dict2)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------