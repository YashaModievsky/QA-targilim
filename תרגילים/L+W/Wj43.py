liss = []
count = 0

while count < 7:
    num = int(input("enter number: "))
    liss.append(num)
    count += 1

print(liss)
print(liss.index(max(liss)))
