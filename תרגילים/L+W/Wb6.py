num = int(input("enter grade: "))
sumEven = 0
sumOdd = 0
countEven = 0
countOdd = 0

while 0 <= num <= 100:
    if num > 59:
        sumEven += num
        countEven += 1
    else:
        sumOdd += num
        countOdd += 1
    num = int(input("enter grade: "))
print(sumEven/countEven, sumOdd/countOdd )
