from random import randint
low = 1                                           #הגדרת ערך תחתון ביותר
high = 100                                        #הגדרת ערך עליון ביותר
num = randint(low ,high)                          #הגדרת גבולות מספר רנדומלי על פי ערכים שהוגדרו
print(num)                                        #הדפסת ניחוש של המחשב
guess = input("enter - correct, high, low: ")     #האם הניחוש של המחשב נכון (נכון, גבוה, נמוך)
while guess != "correct":                         #במידה והניחוש אינו נכון
    if guess == "low":                            #אם הניחוש נמוך מידי להגדיר את הערך החדש כlow (הערך הכי נמוך החדש)
        low = num+1
    else:
        high = num-1                              ##אם הניחוש גבוה מידי להגדיר את הערך החדש כhigh (הערך הכי גבוה החדש)
    num = randint(low, high)                      #הגדרת ג"ג חדשם למספר הרנדומלי
    print(num)                                    #הדפסת ניחוש רנדומלי חדש
    guess = input("enter - correct, high, low: ") #הגדרת השווי של הערך החדש

print("correct")
