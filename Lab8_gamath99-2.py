#In this case modules should be imported with aliases
#Due to files circle.py and rectangle.py containing a similar function name which is calc_area()
#without the aliases, python would not recognize which calc_area function to execute. 

import circle as c
import rectangle as r

# Assign a funtion statement that can select the correct value for the loop that will execute
# Filter positive value to execute 

def capture_positive_number(initial):
    # The while loop will repeat until it capture the correct input value under conditions 
    While True: 

        value = input(initial)
    # Use of the method .isdigit to only the digit and ignore the other value 
        if value.isdigit():
            value = float(value)
            if value > 0: 
                return value
            else:
                print("Error: Please enter a positive number.")
        else: 
            print("Error : Please enter a valid number.")



    
    
    

              
    


