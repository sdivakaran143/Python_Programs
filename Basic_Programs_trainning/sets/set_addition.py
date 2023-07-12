set=set({})
sum=0
for i in range(5):
    set.add(int(input("enter the value: ")))

for i in set:
    sum+=i
print(f"sum of the List is {sum}")
print(5 in set)