count = 1
sum = 0

while count<=5:
    num = int(input("enter num: "))
    sum += num%10
    count += 1
print(sum)