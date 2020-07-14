day = int(input("enter day: "))
month = int(input("enter month: "))
year = int(input("enter year: "))

if day in range(1,32) and month in range(1,13) and year in range(1950,2021):
    print(day, "/" ,month, "/" , year%100, sep='')
else:
    print("error")



if 0 > day > 31 and (0 > month > 13) and (1950 > year > 2020):
    print("error")
else: print("the date is ", day, '/', month,'/', year%100, sep='')