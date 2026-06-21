#creation of the file that will help to calculate the area and the circumference of a circle 
#Use of the built-in functions math

import math

#Assign a function statement to calculate the area of a circle by using the radius as argument 
def calc_area(radius):
    # formula for the area of a circle : pi*radius square
    return math.pi * radius ** 2

#Assign a function statement to calculate the circumference of a circle by using the radius as argument
def calc_circumference(radius):
    #Formula for the circumference of a circle : 2*pi*radius
    return 2 * math.pi * radius
