from sys import argv

script, filename  = argv
count = 0
fileline = open (filename , 'r')
print(f"here are the contents of {filename}:\n ")
for i in fileline.readlines():
    print (i)
    count = count + 1


print (f"there are {count} lines in {filename}")
