num1 = int (input ('please enter a number: '))
num2 = int (input('please enter another number: '))

def compare (val1,val2):
    if (val1 > val2):
        print(f"{val1} will be devided by {val2} , ")
        result = val1 / val2
    elif (val2 > val1):
        print(f"{val2} is greater than {val1} , {val1} will be multiplyed by 10")
        result = val1 * 10

        print(f"the result is: {result}")

    else:
        print(f"both values are the same, no action will be taken")

x = compare (num1 ,num2)
