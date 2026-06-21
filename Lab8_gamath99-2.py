#In this case modules should be imported with aliases
#Due to files circle.py and rectangle.py containing a similar function name which is calc_area()
#without the aliases, python would not recognize which calc_area function to execute. 

import circle as c
import rectangle as r

# Assign a funtion statement that can select the correct value for the loop that will execute
# Filter positive value to execute 

def capture_positive_number(initial):
    # The while loop will repeat until it capture the correct input value under conditions 
    while True:
        try:
            
            value = float(input(initial))
    # Use of the method .isdigit to only the digit and ignore the other value 
            if value <=0: 
                print("Error: Please enter a positive number.")
            else:
                return value                
        except ValueError:
            print("Error : Please enter a valid number.")

# create a while loop to capture the user input to evaluate each statement in return the result. 

selection = 0 

while selection != 5: 

    print("\nGeomery Calculator")
    print("-------------------")
    print("1. Calculate Circle Area")
    print("2. Calculate circle circumference")
    print("3. Calculate Rectangle Area")
    print("4. Calculate Rectagle Perimeter")
    print("5. Exit")

    try:
        selection =int(input("\nEnter your choice (1-5): "))
    #create a filter to select the exact value in the conditions 
        if  selection == 1:
            radius = capture_positive_number("\nEnter the radius of the circle: ")
            #call the alias of the function in circle file to evaluate the area of the circle 
            area = c.calc_area(radius)

            print(f"\nThe area of the circle is {area:.3f}.")
        
            input("\nPress Enter to continue...")
        elif selection == 2:
            radius = capture_positive_number("\nEnter the radius of the circle: ")
            #call the alias of the function in circle file to evaluate the circumference of the circle 
            circumference = c.calc_circumference(radius)

            print(f"\nThe circumference of the circle is {circumference:.3f}.")
            input("\nPress Enter to continue...")
        elif selection == 3:
            width = capture_positive_number("\nEnter the width of the rectangle: ") 

            height = capture_positive_number("Enter the height of the rectangle: ")
            #call the alias of the function in rectangle file to evaluate the area of the rectangle 
            area = r.calc_area(width,height)

            print(f"\nThe area of the rectangle is {area:.3f}")

            input("\nPress Enter to continue...")
        elif selection == 4:
            width = capture_positive_number("\nEnter the width of the rectangle: ")
            height = capture_positive_number("Enter the height of the rectangle: ")
            #call the alias of the function in rectangle file to evaluate the perimeter of the rectangle 
            perimeter = r.calc_perimeter(width,height)
            print(f"\nThe perimeter of the rectangle is {perimeter:.3f}.")

            input("\nPress Enter to continue...")
        elif selection == 5:
            print("\nGoodbye!")
        else:
            print("\nError: Please enter a number between 1 and 5.")
    
    # Request a new value if it is not a digit 
    except ValueError:
        print("\nError: Please enter a valid menu choice.")


    
    
    

              
    


