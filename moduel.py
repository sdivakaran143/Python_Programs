#module 
import mymod as m 
m.tables(1)

import platform 
print(platform.system())

from mymod import person
print(person["key1"])

from mymod import li
print("li",li[1])

import random
print("you random seat number is :",random.randrange(60))


#import my mod test line 
m.name("divakaran")
print(m.li[5])
print(m.person["key1"])

#reversre string 
st="divakaran"
print(st[::-1])


# remove duplicates in list 
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist) 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import camelcase

c = camelcase.CamelCase()

txt = "divan chakaravarthi"

print(c.hump(txt))

#This method capitalizes the first letter of each word.
