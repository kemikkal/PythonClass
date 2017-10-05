radius = 5
volume = (4/3)*(3.14*(radius*radius*radius))
print(f"the volume of a sphere with a radius of {radius} is {volume}")





val = input("please enter a number\n>")
#if the users input is divisible by 3 then print this statement
if (int(val) % 3 == 0):
    print(f"the number {val}  is divisible by 3")

else:
    print(f"{val} is not divisible by 3")


#imports the time library
import time
#creates a variable and assigns it to the current time
now = time.strftime("%c")
## date and time representation
print (f"the date and time is {now}")


user_input = input("type something.\n")
letter =input("what letter would you like me to search for?\n>")
def l_check(string,letter):
    count = 0
    for x in string:
        if letter in x:
            count = count +1

    return count

result = l_check(user_input,letter)

print (f"the letter {letter} appears {result}")




user_i = input("type something.\n")

def l_count(string):
    count = 0
    for x in string:

            count = count +1

    return count

r = l_count(user_i)

print (f"there are {r} letters in your statement")
