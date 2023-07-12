file=open("F:/Python_Programs/Basic_Programs_trainning/basic File operations/file.txt")
file1=file.read()
file.close()

file=open("F:/Python_Programs/Basic_Programs_trainning/basic File operations/file.txt")
file2=file.read()
file.close()

file=open("F:/Python_Programs/Basic_Programs_trainning/basic File operations/file.txt","w")
file.write(file1+"\n")
file.write(file2)
file.close()
