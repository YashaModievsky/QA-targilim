password = input("enter password: ")
password2 = input("enter password again: ")
count = 1
while password2 != password:
    password2 = input("wrong! enter password again: ")
    count += 1
    if count == 5:
        print("cancled, too many tries!")
        break
if password == password2:
    print("welcome!")