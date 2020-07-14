num = int(input("please enter you num: "))
list = []


for i in range(num):
    if i == 0:
        list.append(0)
    elif i == 1:
        list.append(1)
    else:
        list.append(list[i-1]+list[i-2])
print(list)
