#classes defining different shapes with calculations on the parameter and area of each
class Triangle(object):
    def __init__(self, s1, s2, s3, h):
        self.side_a = s1
        self.side_b = s2
        self.side_c = s3
        self.height = h

    def tri_param(self):
        param = self.side_a + self.side_b + self.side_c

        print (f"the parameter of a triangle with sides {self.side_a},{self.side_b},{self.side_c} is {param}")


    def tri_area(self):

        area = (self.side_b * self.height) / 2
        print (f"the area of a triangle with a base of{self.side_b}, and a height of {self.height}, is {area}")
    def __init__(self, s1 , s2):
        self.length = s1
        self.width = s2

class Retangle(object):
    def __init__(self, s1 , s2):
        self.length = s1
        self.width = s2

    def ret_param(self):
        param = (self.length  * 2) + (self.width * 2)

        print (f"the parameter of a retangle with  a width of {self.width}, and a height of {self.length}, is {param}")

    def ret_area(self):
        area = (self.length  * self.width)
        print (f"the parameter of a retangle with sides {self.length},{self.width} is {area}")


class Square (object):
    def __init__(self,s1):
        self.side = s1

    def squ_param(self):
        param = (self.side * 4)

        print(f"the parameter of a square with sides {self.side} is {param}")

    def squ_area(self):
        area = (self.side ** 2)
        print(f"the area of a square with the sides {self.side} is {area}")


class Circle (object):
    def __init__(self,r):
        self.radius = r


    def cir_param(self):
        param = (2 * 3.14) * self.radius

        print(f"the parameter of a circle with a radius of {self.radius} is {param}")

    def cir_area(self):
        area = (self.radius ** 2)  * 3.14

        print(f"the are of a circle with the parameter of {self.radius} is {area}")

#asks the user to input a number as a selection
select = input('1 for triangle calculations \n2 for circle calculations\n3 for retangle calcultions\n4 for square calculations\n>>')
#if the enters a number between 1 and 4 the the code runs
if int(select) > 0 and int(select) < 5:
    #if the user enters 1 it will find the parameter, 2 will find the area
    if select == "1":
        print("you have selected a triangle, would you like to calcuate the area or parameter (press 1 for area, 2 for parameter")
        option = input('>')
        #checks if the user entered a valid operations
        if option == '1' or option =='2':
            s1 = 0
            s2 = 0
            s3 = 0
            h = 0
            if option == '2':
                s1 = int(input('please enter side 1: '))
                s2 = int(input('please enter side 2: '))
                s3 = int(input('please enter side 3: '))
                #calls the function in the class to perform the operation
                p = Triangle(s1,s2,s3,h)
                p.tri_param()
                #displays the result to the user.


            else:
                b = int(input('please enter the base of the triangle: '))
                h = int(input('please enter height of the triangle: '))


                a = Triangle(b,h,s3,h)
                a.tri_area()

        else:
            print("invalid selection")


    elif select == "2":
        print("you have selected a circle, would you like to calcuate the area or parameter (press 1 for area, 2 for parameter")
        option = input('>')
        if option == '1' or option =='2':
            if option == '1':
                r= int(input('please enter the radius of the circle: '))


                p = Circle(r)
                p.cir_area()

            else:
                r = int(input('please enter the radius of the circle: '))



                a = Circle(r)
                a.cir_param()

        else:
            print("invalid selection")




    elif select == "3":
        print("you have selected a retangle, would you like to calcuate the area or parameter (press 1 for area, 2 for parameter")
        option = input('>')
        if option == '1' or option =='2':

            if option == '1':
                s1 = int(input('please enter side 1: '))
                s2 = int(input('please enter side 2: '))
                p = Retangle(s1,s2)
                p.ret_area()


            else:
                b = int(input('please enter the length of the retangle: '))
                h = int(input('please enter the width of the retangle: '))

                p = Retangle(b, h)
                p.ret_param()

        else:
            print("invalid selection")

    elif select == "4":
        print("you have selected a square, would you like to calcuate the area or parameter (press 1 for area, 2 for parameter")
        option = input('>')
        if option == '1' or option =='2':
            if option == '1':
                s1 = int(input('please enter side: '))

                p = Square(s1)
                p.squ_param()


            else:
                s1 = int(input('please enter the side of the square: '))

                a = Square(s1)
                a.squ_area()

        else:
            print("invalid selection")



else:
    print("you have entered an invalid option,script will now close..........................................")
