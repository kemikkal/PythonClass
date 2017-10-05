
class retangle (object):
    def __init__(s1,s2):
        self.length = s1
        self.width = s2

    def ret_area(length,width):
        area = (length * width)
        return area

length = int(input('enter a length for the retangle: '))
width = int(input('\nnow enter the width: '))

area = retangle.ret_area(length,width)

print(f"\nthe area is {area}")
