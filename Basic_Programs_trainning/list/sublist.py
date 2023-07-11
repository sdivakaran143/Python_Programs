allis=[]
def split(li,h):
    # print(type(h))
    # if(len(li)==1):
        # return li
    # allis.append(li)
    # allis.append(li[int(len(li)/h):])
    # split(li[:int(len(li)/h)],h)
    # split(li[int(len(li)/h):],h)
    for i in range(0,len(li)):
        for i in range(i,len(li),h):
            if(len(li[i:i+h])==h):
                allis.append(li[i:i+h])
 

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# list=[range(1,21)]
split(list,5)
print(allis)