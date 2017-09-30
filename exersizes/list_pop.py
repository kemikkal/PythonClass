#creates a string variable with data in it
ten_things ="apples oranges crows telephone light sugar"
print ("adding more things")
#creates a list variable called stuff using the ten_things variable as data
# .split(' ') separates each entry in the list when theres is a space
stuff = ten_things.split(' ')
#initializing a string list
more_stuff = ["Day", "Night", "Song", "Frisbee",
                "Corn", "Banana", "Girl", "Boy"]

#while loop will keep running as the length of stuff is not equal to 10
while len(stuff) !=10:
    #removes the last item in the more_stuff list and saves that
    #value in a variable
    next_one = more_stuff.pop()
    print("adding: ",next_one)
    #adds the data of next_one to the stuff list
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now.\n")


print("there we go: ", stuff)
#prints the second item in the stuff list
print(stuff[1])
#prints the second to last item in the stuff list
print(stuff[-1])
print(stuff.pop())
#seperates the list with spaces
print(' '.join(stuff))
#separates the 4th item and the 6th item with a number sign
print('#'.join(stuff[3:5]))
