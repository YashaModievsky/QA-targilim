from random import randint                                              #מחשק ניחושים

print("WELCOME TO THE GUESSING GAME!")
guess = int(input("please enter your guess(between 1 and 9): "))        #המשתמש מכניס ניחוש

num = randint(1,9)                                                      #התוכנה מגרילה מספר מ1 עד 9
while guess != num and (guess<9 or guess>1):                            #כל עוד הניחוש אינו המספר שהוגרל
    if guess>9 or guess<1:                                              #אם הוא מחוץ לג"ג ישר "נכשל" ומבקש מספר חדש
        print("number is invalid - enter another: ")
    else:
        if guess > num:                                                 #אם הניחוש גדול מהמספר אז להכניס נמוך יותר
            print("enter lower")
        else:
            print("higher")                                             #אםה ניחוש קטן מהמספר אז להכניס מספר גדול יותר
    guess = int(input("please enter your guess(between 1 and 9): "))
print(num)                                                              #הדפסת המספר
print("you are right!")
