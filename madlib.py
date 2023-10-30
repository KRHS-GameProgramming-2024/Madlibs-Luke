from getters import *
from story1 import *
from screens import *

def madlibs(debug = False):
    if debug: print("Welcome to the debug!")

    print(titlescreen(debug))
    try:
        input("press enter to continue")
    except:
        pass
    
    done = False

    while not done:
        print(MainMenu(debug))
        print("\n")
        choice = GetMenuOptions(debug)
        
        if choice == "q":
            exit();
        elif choice == "1":
            print("story 1")
            input("press enter to continue")
            story1()
        elif choice == "2":
            print("story 2")
            input("press enter to continue")
        elif choice == "3":
            print("story 3")
            input("press enter to continue")


madlibs(True)
