#accepts arguments
from sys import argv

#assigns the user input to a variable

option = input('press k to convert from KB to B\npress m to convert from MB to B\npress t to convert from TB to b\npress a to convert from TB to MB\n>>')

def conversion (o):

    if (o == "k"):
        val = input("please enter the value : ")
        result = int(val)*1000
        print(f"{val} kilobytes converted into bytes is {result} bytes")

    elif (o == "m"):
        val = input("please enter the value : ")
        result = int(val)*1000000
        print(f"{val} megabytes converted into bytes is {result} bytes")
    elif (o == "t"):
        val = input("please enter the value : ")
        result = int(val)*1000000000000
        print(f"{val} terabytes converted into bytes is {result} bytes")
    elif (o == "a"):
        val = input("please enter the value : ")
        result = int(val)*1000000
        print(f"{val} terabytes converted into megabytes is {result} megabytes")
    else:
        print("the option entered is not valid, please enter a valid option")


conversion(option)
