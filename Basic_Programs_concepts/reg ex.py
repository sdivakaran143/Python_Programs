import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The golden days"
x = re.search("^The*.days$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

txt="The loard divakaran s day"

x=re.findall("[a-f]", txt)
print(x)
x=re.findall("d.......n", txt)
print(x)
#^^^^^^^^^^^^^^^^^^^^^
x = re.findall("^The", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
#********************
x = re.findall("The*", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
#++++++++++++++++++++++++
x = re.findall("d+", txt)
print(x)
#|||||||||||||||||||||||

x = re.findall("The|the+", txt)

if x:
  print("YES! We have a match!",x)
else:
  print("No match")

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#search

x=re.search("divakaran", txt)
print(x)
if x:
  print("YES! We have a match!")
else:
  print("No match")

x=re.search("\s", txt)
print("whitespace are detected at the position:",x.start())
#---------------------------------------------------------------------------------------------------------------------------------------------------------

#reg ex split
x=re.split("\s", txt)
print(x)

x=re.split("\s", txt, 2)
print(x)

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#sub() replace 
x=re.sub("d", "D", txt)
print(x)
x=re.sub("d", "D", txt,2)#replACE   ONLY FIRST TWO OCCURENCE 
print(x)

x=re.search("di", txt)
print(x.span())
print(x.string)
print(x.group())
