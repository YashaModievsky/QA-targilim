num1 = int(input("enter first: "))
num2 = int(input("enter second: "))

for i in range(num1+1, num2):
    if i%2 == 0:
        print(i)