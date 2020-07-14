dd = int(input("enter day: "))
mm = int(input("enter month: "))
yyyy = int(input("enter year: "))

print("the date is ", dd,"/",mm,"/",yyyy//10%10*10+yyyy%10, sep="")
