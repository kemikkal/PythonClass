from sys import exit

def gold_room():
    print("This room is full of gold, How much do you take?")

    choice = input(">")

    if "0" in choice or "1" in choice:
        how_much = int(choice)

    else:
        dead("man, learn how to type a number.")

    if how_much < 50"
        print("nice, your not greedy, you win")
        exit(0)

    else:
        dead("you greedy bastard!")


def bear_room():
    print("""There is a bear here.
    the bear has a bunch of honey.
    the fat bear is in front of another door.
    how are you going to move the bear?""")
    bear_moved = False

    while True:
        choice = input("> ")
        if choice == "take honey":
dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
         print("The bear has moved from the door.")
         print("You can go through it now.")
         bear_moved = True

        elif choice == "taunt bear" and bear_moved:
            dead("the bear gets pissed off and chews your leg off.")

        elif choice =="open door" and bear_moved:
            gold_room()

        else:
            print("i got no ideaf what that means.")

def cthulhu_room():
    print("here you see the great evil cthulhu")
    print("he, it stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice =input(">")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty")
    else:
        cthulhu_room()

def dead(why):
    print(why, "good job")
    exit(0)

def start():
    print("you are in a dark room")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input (">")

    if choice == "left":
        bear_room()
    elif chice =="right":
        cthulhu_room()
    else:
        dead("you stumble around the room until you starve.")

start()
