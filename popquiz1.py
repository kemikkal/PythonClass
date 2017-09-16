from sys import argv

script = argv
#creates 3 integer variables
x = int (argv[1])
y = int (argv[2])
z = int (argv[3])
#function that takes 3 arguments
def add_2_returns1 (x,y,z):
    #creates a variable that adds the first and the third argument
    num1_3 = x + z
    #creates a variable that stores the second number
    num2 = y
    #returns the second number
    #prints the sum of the argument 1 and 3
    print (f"the sum of {x} and {z} is: {num1_3}")
    return num2
#saves the return value of the function in y
y= add_2_returns1(x,y,z)
print(f"the second number in the list is {y}\n ")
