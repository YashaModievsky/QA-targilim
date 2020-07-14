num = int(input("enter number: "))
list = []
while 0<=num<=100:
    list.append(num)
    num = int(input("enter number: "))
    if 0>num or 100<num:
        print(max (list), '\n', sum(list)/len(list), '\n', (max (list))-(sum(list)/len(list)))
