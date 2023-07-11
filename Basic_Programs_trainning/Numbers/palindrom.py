str=input("enter the string :")
str2=str[::-1]
if(str in str2):
    print(f"the string {str} is palindrome")
else:
    print(f"the string {str} is not  palindrome")

print(f"reverse of the given string {str} is {str2}")