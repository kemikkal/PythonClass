#Imports arguments for use
from sys import argv
#taking the arguments given and assigning them to a variable
script, sor , dest = argv
#opening the sor argument and saving to a variable
s = open(sor,'r')
print(f"this is whats in {sor}:\n")
#reading the content of the sor argument and assigning to a vairiable
sread = s.read()

print (f"{sread} will be added to {dest}\n")


s.close()

#opening the dest argument with write permissions
d = open(dest,'a')
#writing the contents of sor on dest
d.write(sread)
d.close()

print (f"the contents of {dest} is:\n")

#reopening the dest argument
dopen = open(dest,'r')

#reading the contents of dest and displaying it
dis= dopen.read()
print (f"{dis}")

dopen.close()
