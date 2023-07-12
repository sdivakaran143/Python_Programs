import os
# write in file 

file=open("F:/Python_Programs/Basic_Programs_trainning/basic File operations/file.txt","a")
file.write("the second line is written by the python code")
file.close()

# read operation 
# file=open("F:/Python_Programs/Basic_Programs_trainning/basic File operations/file.txt","r")
# print(file.read())
# file.close()

#  remove operation 

# os.remove("F:/Python_Programs/Basic_Programs_trainning/basic File I&O operations/file.txt")
# if os.path.exists("F:/Python_Programs/Basic_Programs_trainning/basic File I&O operations/file.txt"):
#     os.remove("F:/Python_Programs/Basic_Programs_trainning/basic File I&O operations/file.txt")
# else:
#     print("File does not found")

# os.rmdir("F:/Python_Programs/Basic_Programs_trainning/basic File I&O operations/waste")