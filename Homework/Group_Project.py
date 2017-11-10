import random
import os
import sys

lives = 3
car_brand = ""
price = dict()
#this dictionary contains the price of all the different cars in the game
price = {0:[2,4,5,7,9],1:[2,3,5,3,4],2:[3,4,5,3,5],3:[4,5,3,5,6],4:[5,5,9,2,1],5:[6,1,1,1,6]}
mini_items = {0:["Apple Airpod","159","199"],1:["Washing Machine","1520","999"],2:["Cheap pair of beats headphone","45","120"],3:["Scooter","101","115"]}

#saving each price value for future use
pposition =[0,0,0,0,0]
#the range 0-5 match up with a car make and model
car = random.randint(0,5)
#a dictionary to represent rows and colums that will have the price of the car in each row, then the rest of the 0s will be filled up with random numbers
grid = {0:[0,0,0,0,0],
         1:[0,0,0,0,0],
         2:[0,0,0,0,0],
         3:[0,0,0,0,0],
         4:[0,0,0,0,0]}
os.system('clear')
name = input("WELCOME TO PRICEFINDER!\n\nIn order to win you must guess the price of a specifed car starting from the\nfirst number in the price to the last; 5 guesses in total. If you guess wrong\nyou must earn the right to play again by winning the minigame, you only get three chances.\nGOOD LUCK!\n\nWhat is your name? ")
os.system('clear')
    #the numbers 0-5 in the car variable represent car brands and the price of that car.
if car == 0:
    car_brand = "HONDA CIVIC"
    print(f"HELLO {name}, In order to win you must guess the price of a {car_brand} from the grid below row by row")
elif car ==1:
    car_brand = "TOYOTA CAMERY"
    print(f"HELLO {name}, In order to win you must guess the price of a {car_brand} from the grid below row by row")
elif car ==2:
    car_brand = "AUDI A 4"
    print(f"HELLO {name}, In order to win you must guess the price of a {car_brand} from the grid below row by row")
elif car ==3:
    car_brand = "BMW 4 SERIES"
    print(f"HELLO {name}, In order to win you must guess the price of a {car_brand} from the grid below row by row")
elif car ==4:
    car_brand = "LEXUS GS 350"
    print(f"HELLO {name}, In order to win you must guess the price of a {car_brand} from the grid below row by row")
elif car ==5:
    car_brand = "PORCHE CAYENNE"
    print(f"HELLO {name}, In order to win you must guess the price of a {car_brand} from the grid below row by row")



#print(car)#testing purposes , will be commented out for submission
#a functin that place the price of the care in a random colomn of the grid for each row
def pgrid():

    #loops for the length of the price list in the price dictionary
    for i in range (0, len(price[car])):

        #assigns the data in the price dictionary with the same index as the car variable and the same list index as the counter to a random location in the row
        grid[i][random.randint(0,4)] = price[car][i]
        #a list with number 0 - 9 to be used to prevent excessive duplicates
        numlist = [0,1,2,3,4,5,6,7,8,9]
        numlist.remove(price[car][i])
        #loop through each index in the row
        for x in range (0,5):
            if grid[i][x] == price[car][i]:
                test = "true"


            else:
                col = random.choice(numlist)
                #radomly chooses a number from the list to fill up the row.
                grid[i][x] = col
                numlist.remove(col)
    #displays the dictionary in a grid format
    print(f"row 1: {grid[0]}\nrow 2: {grid[1]}\nrow 3: {grid[2]}\nrow 4: {grid[3]}\nrow 5: {grid[4]}\n")



#function for the main game
def pricefinder():

    #counter for the while loops
    count = 0
    player_price = "$"

    winner = "FALSE"
    while winner != "TRUE":#loopes while this statement is not true
        while count < 5:#loops for the amount of rows there are in the grid

            print(f"\nyou are now on row {count + 1}\n{grid[count]}\n")
            #propts the user to enter a value
            user = (input(f'enter a number from the row which you think is the next number in the price of the car\n>'))
            #if the user doesnt enter a number, they will be propted to enter again until a number is entered
            while user != "1" and user != "2" and user != "3" and user != "4" and user != "5" and user != "6" and user != "7" and user != "8" and user != "9" and user != "0":
                user = input("invalid option please choose a single digit number between 0 - 9:  ")

            if  int(user) != price[car][count] :#checks if the user input is correct, if incorrect , minigame function will run
                if lives != 0: #will run the the code below if the user has lives left.
                    print("wrong answer, play the minigame for another shot.\n")
                    item_number = random.randint(0,3)#chooses a random minigame item
                    attempt = items(name)#assigns a varialbe the items class and passes the users name
                    attempt.minigame()#runs the minigame.
                else:
                    sys.exit(f"You have lost all your lives, thanks for playing")
            else:

                count = count + 1
                #adds the users input as the final price to display if they win
                player_price += str(user)



        winner = "TRUE"
    os.system('clear')
    print(f"the price of the {car_brand} is {player_price} dollars congrats!!!")

#Mini game portion of Group Project, this runs if the user guesses wrong
class items(object):
    def __init__(self,pname):

        self.name = pname
    def minigame(self):
        global lives #declares a global variable for use to be called later in the function

        name = self.name

        print(f"You have {lives} lives left\n\nIn order to stay in the game, {name}, you have to enter the price of one of our household items.")
        item_number = random.randint(0,3)

        #this if statment randomizes the position of the answer, so that the same answer isnt in the same position
        ans1 = random.randint(1,2)
        if ans1 ==2:
            ans2 = 1
            rprice = mini_items[item_number][ans1]
            wprice = mini_items[item_number][ans2]
        else:
            ans2 = 2
            rprice = mini_items[item_number][ans2]
            wprice = mini_items[item_number][ans1]

        print(f"The first item we have up is a {mini_items[item_number][0]} valued at either\n{mini_items[item_number][ans1]} or {mini_items[item_number][ans2]}")
        choice = input("What is the price of this item?    ")
        #this loop continue to run until you lose or guess right
        x = 1
        #print(rprice,wprice,choice)#for testing purposes
        while x != 0:
            #prevents the user from entering an invalid option
            if choice != rprice and choice != wprice:





+ -


















                choice = input(f"Input error!. Make sure you are typing in one of the two prices for the item\nplease enter one of the values\n")

            else:
                #nested infinite loop
                while x!=0:
                    #if the user lost all their lives then the game ends
                    if lives == 0:
                        break
                    else:

                        if choice == rprice:
                            #every time the user plays they lose a life regardless of weather its right or wrong
                            lives = lives - 1

                            print(f"\n\nYou are correct. You get another chance to choose the next number in the price of the car!\nyou have {lives} lives left\n")
                            return None

                        else:
                            #every time the user plays they lose a life regardless of weather its right or wrong
                            lives = lives - 1
                            print(f"That is incorrect. Bummer! You have {lives} more chances.  Try to guess the price of another item to continue on in the game.\n")
                            #randomies the item
                            item_number = random.randint(0,3)
                            ans1 = random.randint(1,2)
                            if ans1 ==2:
                                ans2 = 1
                                rprice = mini_items[item_number][ans1]
                                wprice = mini_items[item_number][ans2]
                            else:
                                ans2 = 2
                                rprice = mini_items[item_number][ans2]
                                wprice = mini_items[item_number][ans1]
                            choice = input(f"You have {lives} lives left\nwhat is the price of this {mini_items[item_number][0]}?\nis it {mini_items[item_number][ans1]} or {mini_items[item_number][ans2]}\n")
                            if lives == 0 and choice == rprice:
                                #every time the user plays they lose a life regardless of weather its right or wrong
                                lives = lives - 1
                                print(f"You are correct. You get another chance to choose the next number in the price of the car!\nyou have {lives} lives left\n")
                                return None
                            else:
                                break

                if lives == 0:
                    #if the player has no lives then the game ends
                    sys.exit(f"You have lost all your lives, thanks for playing")


pgrid()
pricefinder()
