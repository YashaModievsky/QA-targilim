num = int(input("enter number: "))
list = []
while num != 0:
    if num > 0:
        list.append(num)
    num = int(input("enter number: "))

print(min(list))


