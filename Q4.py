num=[1,2,4,5,7,9,22,10]
i=0
c=0
while i < len(num):
    if num[i]%2==0:
        c+=1
    i+=1
print("Even numbers:",c)