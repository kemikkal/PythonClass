m = 42
s = 42

#creates a function called conver that accepts two parameters to convert minutes to seconds and adds all variables
def conver(minute,sec):
    #converts minutes to seconds then adds the parameters
    seconds = (minute*60)+sec
    return seconds


total = conver(m,s)

print(f"there are {total} seconds in {m} minutes and {s} seconds")




km = 10
#creates a function to convert kilometers to miles
def km_m(kilo):
    miles = kilo / 1.61

    return miles

miles = km_m(km)

print(f"there are {miles} miles in {km}kilometres")

fahrenheit = 83
#creates a function to convert fahrenheit to celsius
def cel_con(f):
    celsius = ((f-32)*5)/9

    return celsius

cel = cel_con(fahrenheit)
print(f"{fahrenheit} degrees fahrenheit to celsius is {cel} degrees")




#imports the math library
import math
#creats a list with 4 numberic values
val = [81,19,16,121]

#creates a function that accepts the list
def Sqroot(n):

    #loops 4 times
    for x in range(0,4):
        #using the built in function math.sqrt() to find the square root of a number
        #n[x] using the counter x as the index posistion of the list
        root = math.sqrt(n[x])

        print (f"the square root of {n[x]} is {root}")

Sqroot(val)


radius = 9
#creates a function to calculate the area
def c_area(r):
    #calculates the area of the parameter and stores it in a value
    area = 3.14*(r*r)

    return area
#calls the function and stores the return value in a variable
ar = c_area(radius)

print(f"the area of a circle with the radius of {radius} is {ar}")



#accepts user input and stores it in a variable
string = input(f"type anything here\n>>")

def check(string):
    #checks if the letter x is in the variable
    if "x" in string:
        print("the letter X is in your text")
    else:
        print("the letter X is not in your text")
#calls the function
check(string)





user_string = input(f"type something here\n>>")

def vowel_check(string):
    #if any vowel is in the variable then it will print this text
    if "a" in string or "e" in string or "i" in string or "o" in string or "u" in string:
        print("there is a vowel in your text")
    else:
        print("there is no vowel in your text")

vowel_check(user_string)
