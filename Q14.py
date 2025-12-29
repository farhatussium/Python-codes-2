word=input("Enter a Word:")
letter=input("Enter a letter:")
c=0
for ch in word:
    if(ch==letter):
       c+=1
print(f"{letter} in {word} is reapeated {c} times.")