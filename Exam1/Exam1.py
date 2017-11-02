#1
import math
x1 =1
x2 =2
y1 =4
y2 =6
def pdistance (x1,x2,y1,y2):
    #calculates the distance
     distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2))

     len1 = x2-x1
     len2 = y2-y1
     print(f"the distance is {round(distance,2)}")
     #checks if the distnaces can make a triangle
     if ((len1**2)+(len2**2)==(round(distance**2,1))) or ((len1**1)+(round(distance**2,1))==(len2**2)) or ((len1**2)+(round(distance**2,1))==(len2**1)):
         print("these distances can form a triangle\n\n")

     else :
         print("no triangle can be formed with these distances\n\n")


pdistance(x1,x2,y1,y2)


#2
string= 'JKLMNOP'
print(f"Question 2\nthe string is {string}")
for i in string:
    #adds the string ack to the contents of i and saves it
    iack = i+'ack'
    print(f"{iack}")

#3
def cumsum(sum):
    x = [cum[0]]
    for i in range (len(cum)-1):
        val = x[i]+cum[i+1]
        x.append(val)
    print(f"the cumulative sum of that list is{x}")
cum = []
for i in range(4):
      cum.append(int(input('enter number ')))

      print(cum)
cumsum(cum)

#4
from sys import argv
script,fname = argv
string = input('enter a word or phrase ')\
#creates dictonary
occ = dict()

#reads though the string letter by letter
for i in string:
    #if its in the dictonary then it adds on, if its not in the dictonary then it creats it
    if i in occ:
        occ[i]=occ[i]+1
    else:
        occ[i]=1
    print(occ)


flist = dict()
fname = open(fname,'r')
a = fname.read
print(a)
for i in fname:
    #reads though the string letter by letter
    for i in fname.read:
        #if its in the dictonary then it adds on, if its not in the dictonary then it creats it
        if i in flist:
            flist[i]=flist[i]+1
        else:
            flist[i]=1
        print(flist)
#5

list1 = ['a','e','i','o','u']
list2 = ['d','e','v','o','n']
def list_check(list1):
    for i in range (len(list1)):
        if list1[i] in list2:
            print('true')
            break

list_check(list1)

#6
from sys import argv

script, file1, file2 = argv

file1 = open (file1,'r')
print(file1.read)
file2 = open (file2, 'a')
file2.write(contenprint()
print(file2.read())

#7


a = int(input('please enter a number for value a '))
n = int(input('please enter a number for value n '))
b = int(input('please enter a number for value b '))
c = int(input('please enter a number for value c '))

def fermat(a,b,c,n):
    if n > 2 and (a**n)+(b**n) == c**n:
        print ('fermat theroem is wrong')
    else:
        print('that doesnt work')


fermat(a,b,c,n)
