#date and time 

import datetime 

x=datetime.datetime.now()
x1=datetime.datetime(2003, 8, 6)
print(x)
print(datetime.datetime(2003, 8, 6))
print("\n\n")
print(x.strftime("Today is \" %d %B %Y \"\n"))

#legal format codes
print(x.strftime("day in full form : %A"))
print(x.strftime("day in short form : %a"))

print(x.strftime("position of the day in the week : %w"))  

print(x.strftime("date : %d"))

print(x.strftime("Month in short form : %b"))
print(x.strftime("Month in full form : %B"))

print(x.strftime("Month in num  : %m"))

print(x.strftime("year short vision : %y"))
print(x.strftime("year in full vision : %Y"))

print(x.strftime("hour in 24 hrs formate : %H"))
print(x.strftime("hour in 12 hrs formate : %I"))

print(x.strftime("Miniute : %M"))
print(x.strftime("seconds : %S"))

print(x.strftime("number of the week in the year  : %U"))

#https://www.w3schools.com/python/python_datetime.asp  for more reference  