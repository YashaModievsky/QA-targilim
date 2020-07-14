sum = 0
count = 0


while count<6:
    num = int(input("enter num: "))
    if num%2 == 0:
       sum += num
    count += 1

print("the sum is ", sum, "and the avg is ", sum/3)

