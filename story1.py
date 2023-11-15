from getters import *

def story1(debug = False):
    if debug: print("story1 function")
    
    print("\n")
    Place1 = input("Enter place name here:")
    friendName1 = input("Enter friend name here:")
    verb1 = input("Enter verb here:")
    verb2 = input("Enter another verb here:")
    lifeForm1 = input("Enter any kind of life form here:")
    adjective1 = input("Enter an adjective here:")
    verb3 = input("Enter another verb here:")
    adjective2 = input("Enter another adjective here:")
    
    print("\n")
    print("one day I was at " + Place1)
    print("I was with a friend named " + friendName1)
    print("I was " + verb1, "while " + friendName1, "was " + verb2)
    print("and then sudenly out of nowhere a masive" + lifeForm1, "appeard")
    print("it was totaly " + adjective1)
    print("we both started " + verb3, "the " + adjective1, lifeForm1)
    print("it was totaly " + adjective2, "best night of my life!")
