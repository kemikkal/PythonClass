#ask the to enter 3 numbers
#save the numbers in a variables
value1 = int (input("please enter the first number\n"))
value2 = int (input("please enter the second number\n"))
value3 = int (input("please enter the third number\n"))
#check to see if those numbers can form tringle
#3+4+5
def theorem(value1,value2,value3):
    if  (value1*value1)+(value2*value2) == (value3*value3):
        print ("it works we have a triangle")

    elif  (value2*value2)+(value3*value3) == (value1*value1):
        print ("it works we have a triangle")
    elif  (value1*value1)+(value3*value3) == (value2*value2):
        print ("it works we have a triangle")

    else:
        print ("this will ")

theorem(value1,value2,value3)
#(a*a)+(b*b) == (c*c)
