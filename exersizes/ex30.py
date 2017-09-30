#creates 3 variablescars, trucks and people and assigns them a numeric vlaue
people = 30
cars = 40
trucks = 15

#does a comparison between cars and people, if there are more cars then the code below will run
if cars > people:
    print("we should take the cars")

#if the statement above is and there are more people than cars then this code will run
elif cars < people:
    print ("we should not take the cars")
#if both statements are false then this code will run
else:

    print ("we can't decide")

if trucks > cars:
    print("that's too many trucks")

elif trucks < cars:
    print("maybe we could take the trucks")

else:
    print("we still cant decide")
#does a comparison, if there are more people than trucks then the code will run
if people > trucks:
    print ("alright, let's just take the trucks")
#if the statement is false then this code will run
else :

    print("fine, let's stay home then")
