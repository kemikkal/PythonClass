#imports argv to accept aguments
from sys import argv
#takes the user imput and store it in val as a string
val = input ("please enter a number\n>")
#creates a function to check for prime numbers
def prime_check (num):
    #if a number i greater than one the do this
    if num > 1:
        #sets 'x' with a value of 2 and increses until x is equal to num
        for x in range (2,num):
            #if num/x does not have a remainer then print the message and end the loop
            if (num % x) == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
    #if the number is equal to or less than 1 then print this
    else:
        print("this is not a valid number\nplease choose a number greater than 1")


prime_check(int(val))
