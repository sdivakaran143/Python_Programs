n=int(input("enter a digit : "))
li=list(str(n))
for i in li:
    if n%int(i)!=0:
        print(f"the value {n} is not divisible by {li}")
        exit(0)
print(f"the value {n} is divisible by {li}")
