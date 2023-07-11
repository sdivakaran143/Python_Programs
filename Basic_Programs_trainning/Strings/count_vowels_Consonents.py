str=input("enter the string : ")
vowels=""
consonent=""
spcharacter=""
num=""
for i in str:
    if i.isalpha():
        if i in "aeiou":
            vowels+=i
        else:
            consonent+=i
    elif i.isnumeric():
        num+=i
    else:
        spcharacter+=i
print(f"there are {len(vowels)} vowels and {len(consonent)} consonants and numbers {num} and {len(spcharacter)} specialCharacters")
print(f"vowels             -> {vowels}")
print(f"consonent          -> {consonent}")
print(f"numbers            -> {num}")
print(f"specialchatracters -> {spcharacter}")