# file=open("F:/Python_Programs/Basic_Programs_trainning/basic File operations/file.txt")
# str=file.read()
# str=str[::-1]
# file.close()

# file=open("F:/Python_Programs/Basic_Programs_trainning/basic File operations/file.txt","w")
# file.write(str)
# file.close()

file=open("F:/Python_Programs/Basic_Programs_trainning/basic File operations/file.txt")
str=""
for line in file:
    for word in line.split():
        str+=word[::-1]+" "
    str+="\n"

file.close()

file=open("F:/Python_Programs/Basic_Programs_trainning/basic File operations/file.txt","w")
file.write(str)
file.close()