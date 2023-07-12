tpl=(1,2,3,5)
tpl2=(5,2,1,3,6)
ctpl1=list(tpl)
ctpl2=list(tpl2)
union=ctpl1+ctpl2
# tpl.sort()

union=tuple(union)
print("union =< ",union)

print("--------------------------------------------")

intersection=[]
len1=len(tpl)
len2=len(tpl2)

len= len1 if len1<len2 else len2
shrttpl= tpl if len1<len2 else tpl2
lrgtpl = tpl if len1>len2 else tpl2

for i in range(len):
    if shrttpl[i] in lrgtpl:
        intersection.append(shrttpl[i])

print("intersection =< ",intersection)

print("--------------------------------------------")

difference=[]
lrg=list(lrgtpl)
shrt=list(shrttpl)
for i in shrttpl:
    if i in lrgtpl:
        lrg.remove(i)
        shrt.remove(i)
difference.extend(lrg)
difference.extend(shrt)
difference=(tuple(set(difference)))
print(difference)
        

    
