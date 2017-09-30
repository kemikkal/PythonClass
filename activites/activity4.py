grade = input("please input your score: ")

def grade_message (x):
    if int(x) > 55 and int(x) < 70:
        print("u gotta try harder than than\nD   -_-")

    elif int(x) > 69 and int(x) < 80:
        print("not bad i guess\n C    >_>")

    elif int(x) > 79 and int(x) < 90:
        print("good stuff\nB    :)")

    elif int(x) > 89 and int(x) <100:
        print("holy Sh*@!\n you studied hard\nA!   :D")

    elif int(x) == 100:
        print("you clearly cheated\n >:()")

    elif int(x) > 100:
        print("if your scoring that high then you shouldnt be in school u alien")
    else:
        print("you should quit that class your taking\nF......ailure")


grade_message(grade)
