
#To find the year is leap year and non leap year

year=int(input("\nEnter a year to find leap year or non leap year : "))
if year%4==0 and year%400==0 and year%100==0:print(year,"is leep year\n")
else:print(year,"is not leep year \n")