#Mini game portion of Group Project
class items(object):
    def __init__(right,wrong,name):
        self.rprice = right
        self.wprice = wrong
        self.name = name

        def minigame(a, t, s):


            print(f"In order to stay in the game, {name}, you have to select the price of one of our household items.")
            print(f"The first item we have up is a {self.name}")
            choice = input("What is the price of the {self.name}: {$159} or $199?\n\n")

            while choice != self.rprice or choice != self.wprice :
                choice = input("Input error.  Make sure you are typing in one of the two prices for the airpod\n please enter one of the value")


            if choice == "159":
                print("You are correct. You win the airpods and you get another chance to choose the next number in the price of the car!\n")
            elif choice == "199":
                print("That is incorrect. Bummer! You have two more chances.  Try to guess the price of another item to continue on in the game.\n")
            
