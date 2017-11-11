#list for question 1
l = []
l.append("")
#list for question 2
l2 = []
#dictionary for question 5
dic2 = {"key 1" : "val 1" , "key 2" : "val 2" , "key 3": "val 3"}
dic3 = dict()
#list for question 15
listofnumbers = [2,4,6,567,34,67,7,2,45,6,7,8,34,7]
def question1(l):


    for i in range (1 , 11):
        l.append(input(f"enter any argument to store in the list this is entry number {i}: "))

    print(f"the contents of the list is\n{l}")

def question2(l2):
    for i in range (9 , 47):
        if i % 2 == 0:

            l2.append(i)
        else:
            continue

    print(f"a list of even numbers from 10 to 46 is: \n {l2}")

def question3():
    dic = dict()

    for i in range (0, 5):
        value = input("please enter a value key: ")
        key = input("please enter your data for that value: ")
        dic[value] = key
    print (f"your data is:\n {dic}")

def question4():
        dic = {"key 1" : "val 1" , "key 2" : "val 2" , "key 3": "val 3"}
        for i in dic:
            print(f"key: {i} , value: {dic[i]}\n\n")



def question5(dictionary):
    if dictionary == {} :
        print (f"This dictionary is empty")
    else:
        print(f"this dictionary is not empty here are the contents\n{dictionary}")

def question6():
    dic = dict()
    text = input("please enter a string: \n")
    unique = "FALSE"
    repeat = "FALSE"
    for i in text:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1

    for i in dic:
        if dic[i] > 1:
            print ("there are elements that appear multiple times in this string")
            repeat = "TRUE"
            break
        else:
            unique = "TRUE"
    if unique == "TRUE" and repeat == "FALSE":
        print("all elements in the string are unqiue")


def question7():
    exempt = [" ",",","."]
    text = input("please enter a string: ")
    for i in text:
        if i in exempt:
            continue
        else:
            print(i)

def question8_9():
    num_list = [3,5,5,3,67,34,67,2,4,7,8,32,6,8,3,78,2,1,6,7,8,4,3,4,6,7,4,2,67,89,5,3]
    even_count = 0
    odd_count = 0
    for i in range (0, len(num_list)):
        if i != 0:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        else:
            continue
    print(f"\n\n{num_list}\n\nthe list above contains {even_count} even numbers and {odd_count} odd numbers")


def question10():
    dic = dict()
    text = input("please enter a string: \n")
    unique = "FALSE"
    for i in text:
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1

    for i in dic:
        print(f"{i} : {dic[i]}\n ")

def cumsum():
    num_list = [3,5,5,3,67,34,67,2,4,7,8,32,6,8,3,78,2,1,6,7,8,4,3,4,6,7,4,2,67,89,5,3]
    #cum_sum will have the initial value of the first element in the previous list because the cumulative sum of the first element is the first value
    cum_sum = [num_list[0]]
    #i am starting at 1 because the first value in the list is already defined
    for i in range (1,len(num_list)):
        #i use i-1 beacause i the loop starts at an index of one, by subtracting 1 i ensure that the element in the new list will be added by the the element one index above in the old list
        cum_sum.append(cum_sum[i-1] + num_list[i])
    print(cum_sum)

def question13():
    count = 0
    text_list = []
    exempt = ["." , "," , "." , " "]
    text = input("enter a word or phrase and i will check if its a palindrone: ")
    for i in text:
        if i in exempt:
            continue
        else:
            text_list.append(i)


    for i in range (0, len(text_list)):
        #compares the the a element a posisition with the inverse posisition of another element
        if text_list[i] == text_list [-1*(i+1)]:
            count += 1
        else:
            continue

    if count == len(text_list):
        print("the string is a palindrone")
    else:
        print("the string is not a palindrone")


def question14():
    x = 3
    y = "24"
    print (f"the sum of {x} and {y} is : {x + int(y)}")

def doubleList(numberlist):
    for i in numberlist:
        print(f"{i} multiplied by 2 is {i * 2}\n")


def main():

    question1(l)
    #question2(l2)
    #question3()
    #for question 5 u can use either dic2 or dic3 to check the code
    #question5(dic2)
    #question6()
    #question7()
    #question8_9()
    #question10()
    #cumsum()
    #question13()
    #question14()
    #doubleList(listofnumbers)

main()
