#creates a function that takes 2 numbers
def add_values (val1,val2):
    #displays the amount of the first number you have
    print(f"the first value is {val1}")
    #displays the amount of the second number you have
    print(f"the second value is {val2}")
    #dispays funny comment about the values
    print(f"it works")

#calls the fuction with the values 8 and 23
add_values(8,3)


#creates 2 varibles with numeric values
number1 = 12
number2 = 4
#calls the previous function using the variables as values
add_values(number1,number2)


#calls previous function, adding two sets of numbers as the values
add_values(12+3 ,13-5)



#calls previous function , adding  previous variables to a values
add_values(number1/4 , number2+number1)
