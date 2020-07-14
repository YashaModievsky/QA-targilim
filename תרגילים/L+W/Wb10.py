num = int(input("enter number: "))
list = []
while num == int(num):
    if num%3 == 0 or num%7 == 0:
        list.append(num)
    num = int(input("enter number: "))
    if num == 0:
        print(len(list))
        break
