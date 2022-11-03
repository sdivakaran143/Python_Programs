#itretor 

t1=("dosa","idly","paroota","puri",)
itr=iter(t1)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print("\n")

s="vanakam"
st=iter(s)
print(next(st))
print(next(st))
print(next(st))
print(next(st))
print(next(st))
print(next(st))
print(next(st))
print("\n")

for i in s:
    print(i,end="")

print("\n")


class num:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration()

myclass = num()
it = iter(myclass)


for i in it:
    print(i,end=" ")