"""Geometry Calculator
Gama MATHURIN
The program is created to return the area and the circumference of a circle, also to return the are and the perimeter of a rectangle, by using aliases from two other file. 
06/21/2026"""

#creation of the file that will help to calculate the area and the perimeter of a rectangle 

# Assign a function statement to calculate the area of a rectangle by using width and height as arguments. 
def calc_area(width,height):
    #formula to calculate the are of a rectangle is width multiply by height 
    return width * height

#Assign a function statement to calculate the perimeter of a rectangle 
def calc_perimeter(width, height):
    #formula to calculate the area of a rectangle is the sum of width and height multiply by 2
    return 2*(width + height)
