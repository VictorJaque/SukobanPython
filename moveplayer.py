import os
def find_player(displaylevel):
     """
This function will find your player on the board
     """
     a = 0
     for i in displaylevel:
         if displaylevel[a] == "@":
            player = a
            break
         a = a + 1
     return(a)

def move_(move, displaylevel): #Moves your player up 1 step
     p = find_player(displaylevel)
     if move == "w":    
         move = -20
     if move == "s":
         move = 20
     if move == "a":
         move = -1
     if move == "d":
         move = 1
     if displaylevel[p + move] == "o" or displaylevel[p + move] == "+":
         if displaylevel[p + move + move] == " ":
             displaylevel[p + move] = "@"
             displaylevel[p] = " "
             displaylevel[p + move + move] = "o"
         elif displaylevel[p + move + move] == ".":
             displaylevel[p + move + move] = "+"
             displaylevel[p] = " "
             displaylevel[p + move] = "@"
     elif displaylevel[p + move] == " " or ".":
         displaylevel[p + move] = "@"
         displaylevel[p] = " "
     return(displaylevel)


def can_move(move, displaylevel): #Checks if your player can move or not
     p = find_player(displaylevel)
     if move == "w":    
         move = -20
     if move == "s":
         move = 20
     if move == "a":
         move = -1
     if move == "d":
         move = 1
     if displaylevel[p + move] == "#":
         print("There's a Trump wall in the way, try again")
         return(False)
     elif displaylevel[p + move] == "o" or displaylevel[p + move] == "+":
         if displaylevel[p + move + move] == "o":
             print("There's an illegal mexican in the way, try again")
             return(False)
         if displaylevel[p + move + move] == "#":
             print("There's a Trump wall in the way, try again")
             return(False)
     return(True)

def move_player(level, displaylevel):
     """
Function that will go through can_move and will let you move thereafter
     """
     move = input("Which direction do you want to go? Up(w), Down(s), Left(a) or Right(d)? ")
     os.system('clear')
     if len(move) > 1 or len(move) == 0:
          print('      ')
          print(' ')
          print(' ')
          return(displaylevel)
     d = can_move(move, displaylevel)
     if d == False:
          print(' ')
          print(' ')
          return(displaylevel)
     elif d == True:
          print('                                  ')
          print(' ')
          print(' ')
          return(move_(move, displaylevel))
         

