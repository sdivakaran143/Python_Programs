#json 

import json

x='{"name":"divakaran","age":19,"dob":2003}'  #json string

j=json.loads(x) # converting to jstr to dict
print(j["age"])
print(json.dumps(j))#converting dict to jstr 


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))

#indent parameter
print("\nindent\n",json.dumps(x,indent=3))
print("\nindent  seperators\n",json.dumps(x,indent=3, separators=(".","=")))
print("\nindent   sort keys \n",json.dumps(x,indent=3, sort_keys=True))
