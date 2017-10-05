#creates a class called Song
class Song(object):
    #defining one attribute in the class called lyrics
    def __init__(self,l):
        #giving the lyrics attribute the data in parameter l
        self.lyrics = l

    #defining a function called sing song
    def sing_song(self):
        #loops through the contents of the lyrics attribute and prints the data
        for line in self.lyrics:
            print(line)

#calls the class and passing a string list as a prameter
bday_song = Song(["Happy Birthday to you ",
                    "I dont want to get sued",
                    "So ill stop right there\n"])


parade_song  = Song (["The rally with the family",
                        "with pockets full of shells"])

#calls the function in the class called object.
bday_song.sing_song()
parade_song.sing_song()
