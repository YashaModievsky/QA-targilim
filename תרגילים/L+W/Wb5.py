num = int(input("enter grade: "))
sum = 0
count = 0

while 0<=num<=100:
    if num>59:
        sum += num
        count += 1
    num = int(input("enter grade: "))

print(sum/count)