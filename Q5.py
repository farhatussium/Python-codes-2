data = [15, 22, 7, 9, 31, 42]
i = 0
x=int(input("Enter a number to search: "))
found=False
while i < len(data):
    if data[i] == x:
        found=True
        break
    i += 1
if found:
    print(f"{x} is found in the list at index {i}.")
else:
    print(f"{x} is not found in the list.")