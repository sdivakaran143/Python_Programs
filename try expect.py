try:
  print("x")
except NameError:
    print("NameError undifined  variable x ")
except:
  print("An exception occurred") 
else:
    print("no error")
finally:
  print("The 'try except' is finished") 

x=1
if x>0:
    pass
    #raise Exception("sorry no number below zeroo")

x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed") 