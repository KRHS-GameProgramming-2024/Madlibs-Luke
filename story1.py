from getters import *

def story1(debug = False):
    if debug: print("story1 function")
    
    print("\n")
    Place1 = getWord("Enter place name here", debug)

    out = "\n"
    out += "one day I was at " + Place1
    
    
    
    
    return out
