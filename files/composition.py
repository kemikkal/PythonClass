class Parent (object):
    def override(self):
        print("parent override()")

class Child (object):
    def override (self):
        print ("Child override()  ")


dad = Parent()
son = Child()

dad.override()
son.override()
