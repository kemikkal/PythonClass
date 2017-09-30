#this exersize a summary of what is learned so far

#creates string with mupltile lines including tabs, and new lines
text = (f"""this line of paragraph has mupltile lines
you can also add a command for a\n new line  by typing
backslash and the letter N
 """)


#prints that sting variable
print (text)
#creates a variable that performs mathematical operations on numbers
seven = (20 /2) - 3
#prints the result
print (f"{seven}\n")
#creates a function that accepts 1 argument
def num_def (num):
    #creates a variable tht multiplies the argument by 500
    mul = num * 500
    #creates a variable that divides the argument by 1000
    div = num / 1000
    #creates a variable that divides the argument by 100
    div_100 = num /100
    #returns all variables creates in first, second , third
    return mul , div , div_100

#creates a variable and assigns it a numeric value that will be used in the above function
num = 10000
#creates 3 variables and assigns them each of the return
#values of the above function
mul_ret , div_ret, div_ret2 = num_def(num)
#prints the previous variable in formatted string
print("this should print the starting variable:{}\n" .format(num) )
#divides the previous variable by 10 and stores it in itself
num = num /10

#creates a variable to save the return variable of the function
result = num_def(num)
#prints the new variable and the 3 values associated with it
print ("value 1:{}\nvalue 2: {}\nvalue 3: {}".format(*result))
