#file handling in python 

#f=open("file.txt","x")
"""
f=open("file.txt","r")
print(f.read())
#print(f.readlines())
for i in f:
    print(i)
f.close()"""
#----------------------------------------------------
"""f=open("file.txt","a")
f.write("Hello! Welcome to file.txt\nThis file is for testing purposes.\nGood Luck!")
f.close()

f=open("file.txt","r")
print(f.read())"""
#----------------------------------------------------
f=open("file.txt","w")
f.write("opps! i removed all content")
f.close()

f=open("file.txt","r")
print(f.read())

#----------------------------------------------------
#to delete the file
#f=open("file.txt","x")
#import os
#os.rmdir("New folder")#to remove folder
#os.remove("file.txt")#to remove file

"""if os.path.exists("file.txt"):#to check  if the file is avialable
    os.remove("file.txt")
    print("file sucessfilly deleted")
else:
    print("The file does not exist")"""
