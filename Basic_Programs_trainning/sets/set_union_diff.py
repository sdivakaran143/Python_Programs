set1={1,2,3,5}
set2={5,2,1,3,6}

union = set()
union.update(set1)
union.update(set2)
print(union)
print("union =< ",union)

print("--------------------------------------------")
intersection=set()
intersection =set1.difference(set2)
print("intersection =< ",intersection)