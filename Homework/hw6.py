#classes defining different shapes with calculations on the parameter and area of each
class triangle(object):
    def __init__(s1,s2,s3,h):
        self.side_a = s1
        self.side_b = s2
        self.side_c = s3
        self.height = h

    def tri_param(s1,s2,s3):
        param = s1 + s2 + s3

        return param

    def tri_area(base,height):
        area = (base * height) / 2
        return area



class retangle (object):
    def __init__(s1,s2):
        self.length = s1
        self.width = s2

    def ret_param(s1,s2):
        param = (s1 * 2) + (s2 * 2)

        return param

    def ret_area(length,width):
        area = (length * width)
        return area


class square (object):
    def __init__(s1):
        self.side = s1

    def squ_param(s1):
        param = (s1 * 4)

        return param

    def squ_area(side):
        area = (side ** 2)
        return area


class circle (object):
    def __init__(r):
        self.radius


    def cir_param(radius):
        param = (2 * 3.14) * radius

        return param

    def ret_area(radius):
        area = (radius ** 2)  * 3.14
        return area


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
            if option == '1':
                s1 = int(input('please enter side 1: '))
                s2 = int(input('please enter side 2: '))
                s3 = int(input('please enter side 3: '))
                #calls the function in the class to perform the operation
                p = triangle.tri_param(s1,s2,s3)
                #displays the result to the user.
                print (f"the parameter of a triangle with sides {s1},{s2},{s3} is {p}")

            else:
                b = int(input('please enter the base of the triangle: '))
                h = int(input('please enter height of the triangle: '))


                a = triangle.tri_area(b,h,)
                print (f"the area of a triangle with a base of{b}, and a height of {h}, is {a}")
        else:
            print("invalid selection")


    elif select == "2":
        print("you have selected a circle, would you like to calcuate the area or parameter (press 1 for area, 2 for parameter")
        option = input('>')
        if option == '1' or option =='2':
            if option == '1':
                r= int(input('please enter the radius of the circle: '))


                p = circle.cir_param(r)
                print (f"the parameter of a circle with a radius of {r}, is {p}")

            else:
                r = int(input('please enter the radius of the circle: '))



                a = circle.cir_param(r)
                print (f"the area of a circle with a radius of {r}, is {a}")
        else:
            print("invalid selection")




    elif select == "3":
        print("you have selected a retangle, would you like to calcuate the area or parameter (press 1 for area, 2 for parameter")
        option = input('>')
        if option == '1' or option =='2':
            if option == '1':
                s1 = int(input('please enter side 1: '))
                s2 = int(input('please enter side 2: '))


                p = retangle.ret_area(s1,s2)
                print (f"the parameter of a retangle with sides {s1},{s2} is {p}")

            else:
                b = int(input('please enter the length of the retangle: '))
                h = int(input('please enter the width of the retangle: '))


                a = retangle.ret_area(b,h)
                print (f"the area of a triangle with a width of {h}, and a height of {b}, is {a}")
        else:
            print("invalid selection")

    elif select == "4":
        print("you have selected a square, would you like to calcuate the area or parameter (press 1 for area, 2 for parameter")
        option = input('>')
        if option == '1' or option =='2':
            if option == '1':
                s1 = int(input('please enter side: '))


                p = square.squ_param(s1)
                print (f"the parameter of a square with side {s1}, is {p}")

            else:
                s1 = int(input('please enter the side of the square: '))



                a = square.squ_area(s1)
                print (f"the area of a square with a side of{s1}, and is {a}")
        else:
            print("invalid selection")



else:
    print("you have entered an invalid option,script will now close..........................................")
