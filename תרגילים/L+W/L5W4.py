count = 0
countInv = 0
list = []

while count<10:
    grade = int(input("enter grade: "))
    for i in range (4):
        if grade < 0 or grade > 100:
            grade = int(input("enter a valid grade: "))
            countInv += 1
            if countInv == 5:
                break
    if 0<grade<100:
        list.append(grade)
        count += 1
    sum(list)
    if count == 10:
        print(sum(list) / 10)
if countInv == 5:
    print("stoping program!")
