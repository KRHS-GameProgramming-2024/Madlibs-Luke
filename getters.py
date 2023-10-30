def GetMenuOptions(debug = False):
    if debug: print("GetMenuOptions function")
    
    goodinput = False
    
    while not goodinput:
        option = input("Plese select an option")
        option = option.lower()
        
        if (option == "q" or 
            option == "quit" or 
            option == "exit"):
                option = "q"
                goodinput = True

        elif (option == "1" or 
            option == "one" or
            option == "storyone" or
            option == "story1" or 
            option == "story 1"):
                option = "1"
                goodinput = True    
                
        elif (option == "2" or 
            option == "two" or 
            option == "story 2" or
            option == "storytwo" or
            option == "story two" or
            option == "story2"):
                option = "2"
                goodinput = True  

        elif (option == "3" or 
            option == "three" or 
            option == "story three" or 
            option == "storythree" or
            option == "story 3" or 
            option == "story3"):
                option = "3"
                goodinput = True      
        else:
            print("Plese select valid input")
    
    return option



def getWord(prompt, debug = False):
    if debug: print("getWord function")
    
    goodinput = False
    
    while not goodinput:
        word = input(prompt)
        goodimput = True
        if isswear(word, debug):
            goodimput = False
            print ("invalid word")
        
        
        
    
    return word


def isswear (word, debug):
    if debug: print("isswear function")
    if word.lower() in swearlist:
        return True
    else:
        return False 
    
swearlist = ["fuck"
             "shit"
             "bitch"
             "cunt"
             "pussy"
             "retard"
             "nigger"
             "fag"
             "faggot"]
