file=open("F:/Python_Programs/Basic_Programs_trainning/basic File operations/file.txt")
set=set()
for line in file:
    set.add(line.replace("\n", ""))
file.close()

file=open("F:/Python_Programs/Basic_Programs_trainning/basic File operations/file.txt","w")
for i in set:
    file.write((i+"\n"))
file.close()