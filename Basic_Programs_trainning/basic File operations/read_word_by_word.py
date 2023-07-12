file=open("F:/Python_Programs/Basic_Programs_trainning/basic File operations/file.txt")
linecount=0
wordcount=0
for line in file:
    for word  in line.split():
        pass
        print(word,end="-")
        wordcount+=1
    print()
    linecount+=1

file.seek(0)   
charcount=0
for line in file:#it doesnt prints the value fix it
    for word  in line:
        pass
        print(word,end="/")
        charcount+=1

print(f"\nthere are {linecount} lines {wordcount} words and {charcount+1} characters")