num = int(input("enter number: "))
if 99 < num < 1000:
    print("the sum is", num%10+num//10%10+num//100)
else: print("error")
