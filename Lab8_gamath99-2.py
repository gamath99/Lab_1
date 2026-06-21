#In this case modules should be imported with aliases
#Due to files circle.py and rectangle.py containing a similar function name which is calc_area()
#without the aliases, python would not recognize which calc_area function to execute. 

import circle as c
import rectangle as r
