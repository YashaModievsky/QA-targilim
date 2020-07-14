num = int(input("enter number: ")) #בדיקת מספר האם הוא ראשוני או שלא
if num<0:
    print("not prime")
while num>0:
    if num%2 == 0 or num%3 == 0 or num%5 == 0 or num%7 == 0 or num%11 == 0 or num%13:
        print("not prime")
    else:
        print("prime")
    break
