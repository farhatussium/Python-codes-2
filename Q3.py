number=[1,12,3,4,10,6]
max=number[0]
i=0
while i<len(number):
    if number[i]>max:
        max=number[i]
    i+=1
print("The maximum number is:",max)