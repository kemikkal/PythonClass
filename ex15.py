from sys import argv

script, filename = argv
#open command is used to open files, in this case whichever file that was passed as an argument
txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read())

print("type the filename again: ")
file_again= input(">")

txt_again= open(file_again) 

print(txt_again.read())
