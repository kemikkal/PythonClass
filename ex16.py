from sys import argv

script, filename = argv
#propts the user to hit enter to continue or ctrl c to cancel
input (f"""we're going to erase {filename}.
If you dont want that, hit CTRL-C (^C).
If you do want that hit RETURN \n ?"""
)

print("Opening the file...")
#creates a variable and opens the file with write prillages to that variable
target = open (filename,'w')
print("Trunkcating the file. Goodbye!")
#removes all content in the file
target.truncate()
print("Now i'm going to ask you for three lines.")
#accets the users input and stores it in variable
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("im going to write these to the file.")
#writes the users input to the file
target.write(line1 + "\n" + line2 + "\n" + line3 "\n")
print("and finally, we close it.")
#closes the file
target.close()
