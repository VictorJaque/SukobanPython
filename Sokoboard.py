def create_level(level): #Creates the level
    x = 0
    y = 0
    d = 0
    teckin = [] #List that contains the index of all the actual characters
    teck = [] #List that contains all the actual characters in the file
    levellist = ["first_level.sokoban", "second_level.sokoban", "third_level.sokoban", "fourth_level.sokoban", "fifth_level.sokoban", "sixth_level.sokoban", "seventh_level.sokoban", "eighth_level.sokoban", "ninth_level.sokoban", "tenth_level.sokoban"]
    with open(levellist[level - 1]) as f: #Opens the file containing level 1
        for rad in f: #Goes through each line of text in he file
            for tecken in rad: #Goes through each character in the line
                x = x + 1
                d = d + 1
                if tecken == '\n': #Makes it so the correct y-axis value is displayed in the list "teck"
                    y = y + 1
                    x = 0
                if tecken != " ":
                    teck.append({'symb': tecken, 'posy': y, 'posx': x + 1})
                    teckin.append(d)
    return(teck, teckin, level)
  
def check(level):
    x = 0
    y = 0
    ll = [] #List that contains everything in the file, including spaces
    levellist = ["first_level.sokoban", "second_level.sokoban", "third_level.sokoban", "fourth_level.sokoban", "fifth_level.sokoban", "sixth_level.sokoban", "seventh_level.sokoban", "eighth_level.sokoban", "ninth_level.sokoban", "tenth_level.sokoban"]
    with open(levellist[level - 1]) as f:
        for rad in f:
            for tecken in rad:
                x = x + 1
                ll.append({'symb': tecken, 'posy': y, 'posx': x})
    al = len(ll) #Variable containing the length of the level as an integer
    return(al) 

def display_level(teck, teckin, al): #Displays the chosen level
    displaylevel = []
    y = 0
    for i in range(al): #Makes a list based on the length of the level, full of spaces
        displaylevel.append(" ")
    for i in teckin: #Replaces the relevant indices with the character that is supposed to be there
        displaylevel[i - 1] = teck[y]['symb']
        y = y + 1
    print("".join(displaylevel)) #Prints a joined version of the list
    return(displaylevel)
def board(level):
    create_level(level) #Creates the level
    teck = create_level(level)[0]
    teckin = create_level(level)[1]
    print("Level:", level)
    print("Good luck! \n")
    goal = []
    check(level)
    al = check(level)
    displaylevel = display_level(teck, teckin, al)
    return(displaylevel)
