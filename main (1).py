import random
import time
#note: print("") is used instead of \n as it makes code clearer (in my opinion while coding), sorry for any inconvenience.
print(".......................................................")
print(".......................................................")
print("..                                                ", end = "")
print("   ..")
print("..   :::::::     ::::::   ::::::   :::::: ::::::  ", end = "")
print("   ..")
print("..   ::     :: ::      :: ::    :: ::     ::   :: ", end = "")
print("   ..")
print("..   ::     :: ::      :: ::    :: ::     ::    ", end = "")
print("::   ..")
print("..   ::.....   ::      :: ::.....  :::::: ::    ", end = "")
print(" ::  ..")
print("..   ::     :: ::      :: :: ::    ::     ::     ", end = "")
print("::  ..")
print("..   ::     :: ::      :: ::  ::   ::     ::     ", end = "")
print("::  ..")
print("..   ::     :: ::      :: ::   ::  ::     ::    ", end = "")
print("::   ..")
print("..   :::::::     ::::::   ::    :: :::::: ::::::", end = "")
print("     ..")
print("..                                                ", end = "")
print("   ..")
print("..    :::::::    ::::::   :::  ::: ::::::  :::::::", end = "")
print("   ..")
print("..   ::        ::      :: :::::::: ::     ::", end = "")
print("         ..")
print("..   ::        ::      :: :: :: :: ::     ::", end = "")
print("         ..")
print("..   ::        ::......:: ::    :: ::::::  ::::::", end = "")
print("    ..")
print("..   ::  ::::: ::      :: ::    :: ::           ::", end = "")
print("   ..")
print("..   ::    ::  ::      :: ::    :: ::           ::", end = "")
print("   ..")
print("..   ::    ::  ::      :: ::    :: ::          :::", end = "")
print("   ..")
print("..    :::::::  ::      :: ::    :: :::::: :::::::", end = "")
print("    ..")
print(".......................................................")
print(".......................................................")
print("")
print("                          ::::")
print("                          ::::")
print("                       ::::::::::")
print("                        ::::::::")
print("                         ::::::")
print("                          ::::")
print("                           ::")
#game logo
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("Hello there player!")
print("And welcome to BoredGames!")
print("This is a game where you can play a multitude of games offline against a bot (with different difficulties),")
print("or pass-and-play with your friends next to you!")
print("")
#greetings
def tictactoewincheck(): #check if a player has won for vs bot
                    global tictactoeend
                    global tictactoeplayer
                    global chosen5
                    time.sleep(1)
                    #below are checks to see if three are in a row, and that they are 'X' or 'O'
                    if tictactoecoords[0] == tictactoecoords[1] == tictactoecoords[2] and tictactoecoords[0] != " ": 
                      if tictactoecoords[0] == tictactoeplayer:
                        print("You win!")
                        tictactoeend = True
                      else:
                        print("Bot wins!")
                        tictactoeend = True
                      chosen5 = True
                    elif tictactoecoords[3] == tictactoecoords[4] == tictactoecoords[5] and tictactoecoords[3] != " ":
                      if tictactoecoords[3] == tictactoeplayer:
                        print("You win!")
                        tictactoeend = True
                      else:
                        print("Bot wins!")
                        tictactoeend = True
                      chosen5 = True
                    elif tictactoecoords[6] == tictactoecoords[7] == tictactoecoords[8] and tictactoecoords[6] != " ":
                      if tictactoecoords[6] == tictactoeplayer:
                        print("You win!")
                        tictactoeend = True
                      else:
                        print("Bot wins!")
                        tictactoeend = True
                      chosen5 = True
                    elif tictactoecoords[0] == tictactoecoords[4] == tictactoecoords[8] and tictactoecoords[0] != " ":
                      if tictactoecoords[0] == tictactoeplayer:
                        print("You win!")
                        tictactoeend = True
                      else:
                        print("Bot wins!")
                        tictactoeend = True
                      chosen5 = True
                    elif tictactoecoords[6] == tictactoecoords[4] == tictactoecoords[2] and tictactoecoords[6] != " ":
                      if tictactoecoords[6] == tictactoeplayer:
                        print("You win!")
                        tictactoeend = True
                      else:
                        print("Bot wins!")
                        tictactoeend = True
                      chosen5 = True
                    elif tictactoecoords[0] == tictactoecoords[3] == tictactoecoords[6] and tictactoecoords[0] != " ":
                      if tictactoecoords[0] == tictactoeplayer:
                        print("You win!")
                        tictactoeend = True
                      else:
                        print("Bot wins!")
                        tictactoeend = True
                      chosen5 = True
                    elif tictactoecoords[1] == tictactoecoords[4] == tictactoecoords[7] and tictactoecoords[1] != " ":
                      if tictactoecoords[1] == tictactoeplayer:
                        print("You win!")
                        tictactoeend = True
                      else:
                        print("Bot wins!")
                        tictactoeend = True
                      chosen5 = True
                    elif tictactoecoords[2] == tictactoecoords[5] == tictactoecoords[8] and tictactoecoords[2] != " ":
                      if tictactoecoords[2] == tictactoeplayer:
                        print("You win!")
                        tictactoeend = True
                      else:
                        print("Bot wins!")
                        tictactoeend = True
                      chosen5 = True
def tictactoebotalgorithm(): #for the tictactoebot to determine the next move, to attack or defend
  global validbotinput
  global tictactoebot
  global tictactoeplayer
  validbotinput = False
  #below are checks to see if the bot almost has 3 in a row, or if the player almost has 3 in a row soon, and acts accordingly, prioritising attack. If none can be found, random input
  while validbotinput == False:
                      if tictactoecoords[0] == tictactoecoords[1] and tictactoecoords[0] == tictactoebot and tictactoecoords[2] == " ":
                        tictactoecoords[2] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[1] == tictactoecoords[2] and tictactoecoords[1] == tictactoebot and tictactoecoords[0] == " ":
                        tictactoecoords[0] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[0] == tictactoecoords[2] and tictactoecoords[0] == tictactoebot and tictactoecoords[1] == " ":
                        tictactoecoords[1] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[3] == tictactoecoords[4] and tictactoecoords[3] == tictactoebot and tictactoecoords[5] == " ":
                        tictactoecoords[5] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[4] == tictactoecoords[5] and tictactoecoords[4] == tictactoebot and tictactoecoords[3] == " ":
                        tictactoecoords[3] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[3] == tictactoecoords[5] and tictactoecoords[3] == tictactoebot and tictactoecoords[4] == " ":
                        tictactoecoords[4] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[6] == tictactoecoords[7] and tictactoecoords[6] == tictactoebot and tictactoecoords[8] == " ":
                        tictactoecoords[8] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[7] == tictactoecoords[8] and tictactoecoords[7] == tictactoebot and tictactoecoords[6] == " ":
                        tictactoecoords[6] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[6] == tictactoecoords[8] and tictactoecoords[6] == tictactoebot and tictactoecoords[7] == " ":
                        tictactoecoords[7] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[0] == tictactoecoords[4] and tictactoecoords[0] == tictactoebot and tictactoecoords[8] == " ":
                        tictactoecoords[8] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[4] == tictactoecoords[8] and tictactoecoords[4] == tictactoebot and tictactoecoords[0] == " ":
                        tictactoecoords[0] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[0] == tictactoecoords[8] and tictactoecoords[0] == tictactoebot and tictactoecoords[4] == " ":
                        tictactoecoords[4] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[2] == tictactoecoords[4] and tictactoecoords[2] == tictactoebot and tictactoecoords[6] == " ":
                        tictactoecoords[6] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[4] == tictactoecoords[6] and tictactoecoords[4] == tictactoebot and tictactoecoords[2] == " ":
                        tictactoecoords[2] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[2] == tictactoecoords[6] and tictactoecoords[2] == tictactoebot and tictactoecoords[4] == " ":
                        tictactoecoords[4] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[0] == tictactoecoords[3] and tictactoecoords[0] == tictactoebot and tictactoecoords[6] == " ":
                        tictactoecoords[6] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[3] == tictactoecoords[6] and tictactoecoords[3] == tictactoebot and tictactoecoords[0] == " ":
                        tictactoecoords[0] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[0] == tictactoecoords[6] and tictactoecoords[0] == tictactoebot and tictactoecoords[3] == " ":
                        tictactoecoords[3] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[1] == tictactoecoords[4] and tictactoecoords[1] == tictactoebot and tictactoecoords[7] == " ":
                        tictactoecoords[7] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[4] == tictactoecoords[7] and tictactoecoords[4] == tictactoebot and tictactoecoords[1] == " ":
                        tictactoecoords[1] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[1] == tictactoecoords[7] and tictactoecoords[1] == tictactoebot and tictactoecoords[4] == " ":
                        tictactoecoords[4] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[2] == tictactoecoords[8] and tictactoecoords[2] == tictactoebot and tictactoecoords[5] == " ":
                        tictactoecoords[5] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[2] == tictactoecoords[5] and tictactoecoords[2] == tictactoebot and tictactoecoords[8] == " ":
                        tictactoecoords[8] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[5] == tictactoecoords[8] and tictactoecoords[5] == tictactoebot and tictactoecoords[2] == " ":
                        tictactoecoords[2] = tictactoebot
                        validbotinput = True 
                        #attack code above
                      elif tictactoecoords[0] == tictactoecoords[1] and tictactoecoords[0] == tictactoeplayer and tictactoecoords[2] == " ":
                        tictactoecoords[2] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[1] == tictactoecoords[2] and tictactoecoords[1] == tictactoeplayer and tictactoecoords[0] == " ":
                        tictactoecoords[0] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[0] == tictactoecoords[2] and tictactoecoords[0] == tictactoeplayer and tictactoecoords[1] == " ":
                        tictactoecoords[1] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[3] == tictactoecoords[4] and tictactoecoords[3] == tictactoeplayer and tictactoecoords[5] == " ":
                        tictactoecoords[5] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[4] == tictactoecoords[5] and tictactoecoords[4] == tictactoeplayer and tictactoecoords[3] == " ":
                        tictactoecoords[3] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[3] == tictactoecoords[5] and tictactoecoords[3] == tictactoeplayer and tictactoecoords[4] == " ":
                        tictactoecoords[4] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[6] == tictactoecoords[7] and tictactoecoords[6] == tictactoeplayer and tictactoecoords[8] == " ":
                        tictactoecoords[8] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[7] == tictactoecoords[8] and tictactoecoords[7] == tictactoeplayer and tictactoecoords[6] == " ":
                        tictactoecoords[6] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[6] == tictactoecoords[8] and tictactoecoords[6] == tictactoeplayer and tictactoecoords[7] == " ":
                        tictactoecoords[7] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[0] == tictactoecoords[4] and tictactoecoords[0] == tictactoeplayer and tictactoecoords[8] == " ":
                        tictactoecoords[8] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[4] == tictactoecoords[8] and tictactoecoords[4] == tictactoeplayer and tictactoecoords[0] == " ":
                        tictactoecoords[0] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[0] == tictactoecoords[8] and tictactoecoords[0] == tictactoeplayer and tictactoecoords[4] == " ":
                        tictactoecoords[4] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[2] == tictactoecoords[4] and tictactoecoords[2] == tictactoeplayer and tictactoecoords[6] == " ":
                        tictactoecoords[6] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[4] == tictactoecoords[6] and tictactoecoords[4] == tictactoeplayer and tictactoecoords[2] == " ":
                        tictactoecoords[2] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[2] == tictactoecoords[6] and tictactoecoords[2] == tictactoeplayer and tictactoecoords[4] == " ":
                        tictactoecoords[4] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[0] == tictactoecoords[3] and tictactoecoords[0] == tictactoeplayer and tictactoecoords[6] == " ":
                        tictactoecoords[6] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[3] == tictactoecoords[6] and tictactoecoords[3] == tictactoeplayer and tictactoecoords[0] == " ":
                        tictactoecoords[0] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[0] == tictactoecoords[6] and tictactoecoords[0] == tictactoeplayer and tictactoecoords[3] == " ":
                        tictactoecoords[3] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[1] == tictactoecoords[4] and tictactoecoords[1] == tictactoeplayer and tictactoecoords[7] == " ":
                        tictactoecoords[7] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[4] == tictactoecoords[7] and tictactoecoords[4] == tictactoeplayer and tictactoecoords[1] == " ":
                        tictactoecoords[1] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[1] == tictactoecoords[7] and tictactoecoords[1] == tictactoeplayer and tictactoecoords[4] == " ":
                        tictactoecoords[4] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[2] == tictactoecoords[8] and tictactoecoords[2] == tictactoeplayer and tictactoecoords[5] == " ":
                        tictactoecoords[5] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[2] == tictactoecoords[5] and tictactoecoords[2] == tictactoeplayer and tictactoecoords[8] == " ":
                        tictactoecoords[8] = tictactoebot
                        validbotinput = True
                      elif tictactoecoords[5] == tictactoecoords[8] and tictactoecoords[5] == tictactoeplayer and tictactoecoords[2] == " ":
                        tictactoecoords[2] = tictactoebot
                        validbotinput = True
                      else:
                        botgeneration = random.randint(0,8)
                        if tictactoecoords[botgeneration] == " ":
                          tictactoecoords[botgeneration] = tictactoebot
                          validbotinput = True
def tictactoeeasymode(): #easy mode tictactoe, where the bot chooses squares at random and player is "X"
  global tictactoeend
  global playerturn
  global validbotinput
  global chosen5
  while tictactoeend == False: #loops until a player wins or draw
                   if playerturn % 2 == 0 and playerturn < 9: #player turn
                      playerturn += 1
                      chosen5 = False
                      tictactoecount = 0
                      coordscount = 0
                      tictactoecount = 0
                      for w in tictactoecoords: #prints the grid
                        tictactoecount += 1
                        if tictactoecount % 3 == 1:
                          print("")
                          print("|",w,"|", end = "")
                        else:
                          print("|",w,"|", end = "")
                      print("")
                      for e in coordslist: #prints all the coordinates
                        coordscount += 1
                        if coordscount % 3 == 1:
                          print("")
                          print("|",e,"|", end = "")
                        else:
                          print("|",e,"|", end = "")
                      print("")
                      print("")
                      tictactoewincheck()
                      print("")
                      while chosen5 == False: #loops until valid input
                        print("Player's turn")
                        print("")
                        inp = input("Enter the coordinate of the tile you would like to click here: ").upper()
                        if inp in coordslist and tictactoecoords[coordslist.index(inp)] == " ": #if input is valid
                          chosen5 = True
                          tictactoecoords[coordslist.index(inp)] = tictactoeplayer
                        else: #input not valid
                          print("")
                          print("Invalid input! Please try again.")
                          print("")
                   elif playerturn == 9: #all nine squares filled
                     tictactoeend = False
                     tictactoewincheck()
                     if tictactoeend == False:
                      print("")
                      print("Draw!")
                      tictactoeend = True
                   else: #bot turn
                     playerturn += 1
                     validbotinput = False
                     tictactoecount = 0
                     for w in tictactoecoords: #prints board
                      tictactoecount += 1
                      if tictactoecount % 3 == 1:
                        print("")
                        print("|",w,"|", end = "")
                      else:
                        print("|",w,"|", end = "")
                     print("")
                     print("")
                     tictactoewincheck()
                     while validbotinput == False: #finds a valid input for the bot to place
                      botgeneration = random.randint(0,8)
                      if tictactoecoords[botgeneration] == " ":
                        tictactoecoords[botgeneration] = tictactoebot
                        validbotinput = True
def tictactoehardmode(): #hard mode tictactoe, where the bot strategically makes moves
  global tictactoeend
  global playerturn
  global validbotinput
  global chosen5
  while tictactoeend == False: #loops till player wins or draw
                   if playerturn % 2 == 0 and playerturn < 9: #player turn
                      playerturn += 1
                      chosen5 = False
                      tictactoecount = 0
                      coordscount = 0
                      tictactoecount = 0
                      for w in tictactoecoords: #prints board
                        tictactoecount += 1
                        if tictactoecount % 3 == 1:
                          print("")
                          print("|",w,"|", end = "")
                        else:
                          print("|",w,"|", end = "")
                      print("")
                      for e in coordslist: #prints coordinates for board
                        coordscount += 1
                        if coordscount % 3 == 1:
                          print("")
                          print("|",e,"|", end = "")
                        else:
                          print("|",e,"|", end = "")
                      print("")
                      print("")
                      tictactoewincheck()
                      print("")
                      while chosen5 == False: #loops till valid input
                        print("Player's turn")
                        print("")
                        inp = input("Enter the coordinate of the tile you would like to click here: ").upper()
                        if inp in coordslist and tictactoecoords[coordslist.index(inp)] == " ": #if input is valid
                          chosen5 = True
                          tictactoecoords[coordslist.index(inp)] = tictactoeplayer
                        else: #if input isnt valid
                          print("")
                          print("Invalid input! Please try again.")
                          print("")
                   elif playerturn == 9: #all nine squares done
                     tictactoeend = False
                     tictactoewincheck()
                     if tictactoeend == False:
                      print("")
                      print("Draw!")
                      tictactoeend = True
                   else: #bot turn
                     playerturn += 1
                     validbotinput = False
                     tictactoecount = 0
                     for w in tictactoecoords:
                      tictactoecount += 1
                      if tictactoecount % 3 == 1:
                        print("")
                        print("|",w,"|", end = "")
                      else:
                        print("|",w,"|", end = "")
                     print("")
                     print("")
                     tictactoewincheck()
                     tictactoebotalgorithm()
def tictactoehardmodeplayer2(): #hard mode tictactoe, where bot strategically makes moves and player plays as "O"
  global tictactoeend
  global playerturn
  global validbotinput
  global chosen5
  while tictactoeend == False: #loops till player wins or draw
                   if playerturn % 2 == 1 and playerturn < 10: #player turn
                      playerturn += 1
                      chosen5 = False
                      tictactoecount = 0
                      coordscount = 0
                      tictactoecount = 0
                      for w in tictactoecoords:
                        tictactoecount += 1
                        if tictactoecount % 3 == 1:
                          print("")
                          print("|",w,"|", end = "")
                        else:
                          print("|",w,"|", end = "")
                      print("")
                      for e in coordslist:
                        coordscount += 1
                        if coordscount % 3 == 1:
                          print("")
                          print("|",e,"|", end = "")
                        else:
                          print("|",e,"|", end = "")
                      print("")
                      print("")
                      tictactoewincheck()
                      print("")
                      while chosen5 == False: #loops till valid input
                        print("Player's turn")
                        print("")
                        inp = input("Enter the coordinate of the tile you would like to click here: ").upper()
                        if inp in coordslist and tictactoecoords[coordslist.index(inp)] == " ":
                          chosen5 = True
                          tictactoecoords[coordslist.index(inp)] = tictactoeplayer
                        else:
                          print("")
                          print("Invalid input! Please try again.")
                          print("")
                   elif playerturn == 10: #all nine squares done
                     tictactoeend = False
                     tictactoewincheck()
                     if tictactoeend == False:
                      print("")
                      print("Draw!")
                      tictactoeend = True
                   else: #bot turn
                     playerturn += 1
                     validbotinput = False
                     tictactoecount = 0
                     for w in tictactoecoords:
                      tictactoecount += 1
                      if tictactoecount % 3 == 1:
                        print("")
                        print("|",w,"|", end = "")
                      else:
                        print("|",w,"|", end = "")
                     print("")
                     print("")
                     tictactoewincheck()
                     tictactoebotalgorithm()
def tictactoepvpwincheck(): #to check if a player has won
                    global tictactoeend
                    global tictactoeplayer
                    global chosen5
                    time.sleep(1)
                    if tictactoecoords[0] == tictactoecoords[1] == tictactoecoords[2] and tictactoecoords[0] != " ":
                      if tictactoecoords[0] == tictactoeplayer:
                        print("Player 1 wins!")
                        tictactoeend = True
                        chosen5 = True
                      else:
                        print("Player 2 wins!")
                        tictactoeend = True
                        chosen5 = True
                        
                    elif tictactoecoords[3] == tictactoecoords[4] == tictactoecoords[5] and tictactoecoords[3] != " ":
                      if tictactoecoords[3] == tictactoeplayer:
                        print("Player 1 wins!")
                        tictactoeend = True
                        chosen5 = True
                      else:
                        print("Player 2 wins!")
                        tictactoeend = True
                        chosen5 = True
                    elif tictactoecoords[6] == tictactoecoords[7] == tictactoecoords[8] and tictactoecoords[6] != " ":
                      if tictactoecoords[6] == tictactoeplayer:
                        print("Player 1 wins!")
                        tictactoeend = True
                        chosen5 = True
                      else:
                        print("Player 2 wins!")
                        tictactoeend = True
                        chosen5 = True
                    elif tictactoecoords[0] == tictactoecoords[4] == tictactoecoords[8] and tictactoecoords[0] != " ":
                      if tictactoecoords[0] == tictactoeplayer:
                        print("Player 1 wins!")
                        tictactoeend = True
                        chosen5 = True
                      else:
                        print("Player 2 wins!")
                        tictactoeend = True
                        chosen5 = True
                    elif tictactoecoords[6] == tictactoecoords[4] == tictactoecoords[2] and tictactoecoords[6] != " ":
                      if tictactoecoords[6] == tictactoeplayer:
                        print("Player 1 wins!")
                        tictactoeend = True
                        chosen5 = True
                      else:
                        print("Player 2 wins!")
                        tictactoeend = True
                        chosen5 = True
                    elif tictactoecoords[0] == tictactoecoords[3] == tictactoecoords[6] and tictactoecoords[0] != " ":
                      if tictactoecoords[0] == tictactoeplayer:
                        print("Player 1 wins!")
                        tictactoeend = True
                        chosen5 = True
                      else:
                        print("Player 2 wins!")
                        tictactoeend = True
                        chosen5 = True
                    elif tictactoecoords[1] == tictactoecoords[4] == tictactoecoords[7] and tictactoecoords[1] != " ":
                      if tictactoecoords[1] == tictactoeplayer:
                        print("Player 1 wins!")
                        tictactoeend = True
                        chosen5 = True
                      else:
                        print("Player 2 wins!")
                        tictactoeend = True
                        chosen5 = True
                    elif tictactoecoords[2] == tictactoecoords[5] == tictactoecoords[8] and tictactoecoords[2] != " ":
                      if tictactoecoords[2] == tictactoeplayer:
                        print("Player 1 wins!")
                        tictactoeend = True
                        chosen5 = True
                      else:
                        print("Player 2 wins!")
                        tictactoeend = True
                        chosen5 = True
def tictactoepvp(): #the code for pass-and-play tictactoe
                  global tictactoeend
                  global playerturn
                  global tictactoeplayer 
                  global tictactoebot
                  global chosen5
                  tictactoeplayer = "X"
                  tictactoebot = "0"
                  while tictactoeend == False: #loops till player wins or draw
                    if playerturn % 2 == 0 and playerturn < 9:
                      playerturn += 1
                      chosen5 = False
                      tictactoecount = 0
                      coordscount = 0
                      tictactoecount = 0
                      for w in tictactoecoords:
                        tictactoecount += 1
                        if tictactoecount % 3 == 1:
                          print("")
                          print("|",w,"|", end = "")
                        else:
                          print("|",w,"|", end = "")
                      print("")
                      for e in coordslist:
                        coordscount += 1
                        if coordscount % 3 == 1:
                          print("")
                          print("|",e,"|", end = "")
                        else:
                          print("|",e,"|", end = "")
                      print("")
                      print("")
                      tictactoepvpwincheck()
                      while chosen5 == False: #loops till valid input
                        print("")
                        print("Player 1's turn")
                        print("")
                        inp = input("Enter the coordinate of the tile you would like to click here: ").upper()
                        if inp in coordslist and tictactoecoords[coordslist.index(inp)] == " ":
                          chosen5 = True
                          tictactoecoords[coordslist.index(inp)] = tictactoeplayer
                        else:
                          print("")
                          print("Invalid input! Please try again.")
                          print("")
                    elif playerturn == 9: #all nine squares done
                     tictactoeend = False
                     tictactoepvpwincheck()
                     if tictactoeend == False:
                      print("")
                      print("Draw!")
                      tictactoeend = True
                    else: #player 2s turn
                     chosen5 = False
                     playerturn += 1
                     tictactoecount = 0
                     for w in tictactoecoords:
                      tictactoecount += 1
                      if tictactoecount % 3 == 1:
                        print("")
                        print("|",w,"|", end = "")
                      else:
                        print("|",w,"|", end = "")
                     print("")
                     for e in coordslist:
                        coordscount += 1
                        if coordscount % 3 == 1:
                          print("")
                          print("|",e,"|", end = "")
                        else:
                          print("|",e,"|", end = "")
                     print("")
                     print("")
                     tictactoepvpwincheck()
                     while chosen5 == False: #loops till valid input
                        print("")
                        print("Player 2's turn")
                        print("")
                        inp = input("Enter the coordinate of the tile you would like to click here: ").upper()
                        if inp in coordslist and tictactoecoords[coordslist.index(inp)] == " ":
                          chosen5 = True
                          tictactoecoords[coordslist.index(inp)] = tictactoebot
                        else:
                          print("")
                          print("Invalid input! Please try again.")
                          print("")
def rockpaperscissorswincheck(): #to check who won in rock paper scissors
  global rockpaperscissorsplayer1
  global rockpaperscissorsplayer2
  global rockpaperscissorsplayer1score
  global rockpaperscissorsplayer2score
  print("")
  print("Player 1 chooses")
  time.sleep(1)
  print(rockpaperscissorsplayer1)
  print("")
  print("Player 2 chooses")
  time.sleep(1)
  print(rockpaperscissorsplayer2)
  time.sleep(1)
  print("")
  if rockpaperscissorsplayer1 == rockpaperscissorsplayer2:
    print("It's a draw!")
  elif rockpaperscissorsplayer1 == "Rock" and rockpaperscissorsplayer2 == "Scissors":
    print("Rock beats Scissors, Player 1 wins!")
    rockpaperscissorsplayer1score += 1
  elif rockpaperscissorsplayer1 == "Paper" and rockpaperscissorsplayer2 == "Rock":
    print("Paper beats Rock, Player 1 wins!")
    rockpaperscissorsplayer1score += 1
  elif rockpaperscissorsplayer1 == "Scissors" and rockpaperscissorsplayer2 == "Paper":
    print("Scissors beats Paper, Player 1 wins!")
    rockpaperscissorsplayer1score += 1
  elif rockpaperscissorsplayer2 == "Rock" and rockpaperscissorsplayer1 == "Scissors":
    print("Rock beats Scissors, Player 2 wins!")
    rockpaperscissorsplayer2score += 1
  elif rockpaperscissorsplayer2 == "Paper" and rockpaperscissorsplayer1 == "Rock":
    print("Paper beats Rock, Player 2 wins!")
    rockpaperscissorsplayer2score += 1
  elif rockpaperscissorsplayer2 == "Scissors" and rockpaperscissorsplayer1 == "Paper":
    print("Scissors beats Paper, Player 2 wins!")
    rockpaperscissorsplayer2score += 1
def battleshipprinting(): #prints both coordinates of player and the list of coordinates for *vs bot*
  global battleshipcoords
  global battleshipcount
  global battleshipcoordslist
  battleshipcount = 0
  for g in battleshipcoords:
                      battleshipcount += 1
                      if battleshipcount % 6 == 1:
                        print("")
                        print("|",g,"|", end = "")
                      else:
                        print("|",g,"|", end = "")
  print("")
  battleshipcount = 0
  for h in battleshipcoordslist:
                        battleshipcount += 1
                        if battleshipcount % 6 == 1:
                          print("")
                          print("|",h,"|", end = "")
                        else:
                          print("|",h,"|", end = "")
def battleshipprintcoordslist(): #prints only the list of coordinates
  global battleshipcount
  global battleshipcoordslist
  battleshipcount = 0
  for h in battleshipcoordslist:
                        battleshipcount += 1
                        if battleshipcount % 6 == 1:
                          print("")
                          print("|",h,"|", end = "")
                        else:
                          print("|",h,"|", end = "")
  print("")
  print("")
def battleshipplayer2print(): #prints both coordinates of player 2 and the list of coordinates for pvp
  global battleshipcount
  global battleshipplayer2coords
  global battleshipcoordslist
  battleshipcount = 0
  for z in battleshipplayer2coords:
                      battleshipcount += 1
                      if battleshipcount % 6 == 1:
                        print("")
                        print("|",z,"|", end = "")
                      else:
                        print("|",z,"|", end = "")
  print("")
  battleshipcount = 0
  for x in battleshipcoordslist:
                        battleshipcount += 1
                        if battleshipcount % 6 == 1:
                          print("")
                          print("|",x,"|", end = "")
                        else:
                          print("|",x,"|", end = "")
  print("")
  print("")
def battleshipplayer1print(): #prints both coordinates of player 1 and the list of coordinates for pvp
  global battleshipcount
  global battleshipcoords
  global battleshipcoordslist
  battleshipcount = 0
  for g in battleshipcoords:
                      battleshipcount += 1
                      if battleshipcount % 6 == 1:
                        print("")
                        print("|",g,"|", end = "")
                      else:
                        print("|",g,"|", end = "")
  print("")
  battleshipcount = 0
  for h in battleshipcoordslist:
                        battleshipcount += 1
                        if battleshipcount % 6 == 1:
                          print("")
                          print("|",h,"|", end = "")
                        else:
                          print("|",h,"|", end = "")
  print("")
  print("")
def battleshipplayer2setup(): #set up the board for player 2
              global chosen4
              global battleshipcoordslist
              global battleshipplayer2coords
              print("")
              print("You have 4 battleships. 2 horizontal, 2 vertical, each have a 2-segment and 3-segment ship each.")
              print("")
              while chosen4 == False: #loops till valid input
                battleshipplayer2print()
                inp = input("Choose where the top segment of your vertical 2-segment ship will be on the grid: ").upper()
                if inp in battleshipcoordslist and "F" not in inp and battleshipplayer2coords[battleshipcoordslist.index(inp)] != "O" and battleshipplayer2coords[battleshipcoordslist.index(inp) + 6] != "O":
                  chosen4 = True
                  battleshipplayer2coords[battleshipcoordslist.index(inp)] = "O"
                  battleshipplayer2coords[battleshipcoordslist.index(inp) + 6] = "O"
                else:
                  print("")
                  print("Invalid input, please try again")
              chosen4 = False
              while chosen4 == False: #loops till valid input
                battleshipplayer2print()
                inp = input("Choose where the top segment of your vertical 3-segment ship will be on the grid: ").upper()
                if inp in battleshipcoordslist and "F" not in inp and "E" not in inp and battleshipplayer2coords[battleshipcoordslist.index(inp)] != "O" and battleshipplayer2coords[battleshipcoordslist.index(inp) + 6] != "O" and battleshipplayer2coords[battleshipcoordslist.index(inp) + 12] != "O":
                  chosen4 = True
                  battleshipplayer2coords[battleshipcoordslist.index(inp)] = "O"
                  battleshipplayer2coords[battleshipcoordslist.index(inp) + 6] = "O"
                  battleshipplayer2coords[battleshipcoordslist.index(inp) + 12] = "O"
                else:
                  print("")
                  print("Invalid input, please try again")
              chosen4 = False
              while chosen4 == False: #loops till valid input
                battleshipplayer2print()
                inp = input("Choose where the leftmost segment of your horizontal 2-segment ship will be on the grid: ").upper()
                if inp in battleshipcoordslist and "6" not in inp and battleshipplayer2coords[battleshipcoordslist.index(inp)] != "O" and battleshipplayer2coords[battleshipcoordslist.index(inp) + 1] != "O":
                  chosen4 = True
                  battleshipplayer2coords[battleshipcoordslist.index(inp)] = "O"
                  battleshipplayer2coords[battleshipcoordslist.index(inp) + 1] = "O"
                else:
                  print("")
                  print("Invalid input, please try again")
                  print("")
              chosen4 = False
              while chosen4 == False: #loops till valid input
                battleshipplayer2print()
                inp = input("Choose where the leftmost segment of your horizontal 3-segment ship will be on the grid: ").upper()
                if inp in battleshipcoordslist and "5" not in inp and "6" not in inp and battleshipplayer2coords[battleshipcoordslist.index(inp)] != "O" and battleshipplayer2coords[battleshipcoordslist.index(inp) + 1] != "O" and battleshipplayer2coords[battleshipcoordslist.index(inp) + 2] != "O":
                  chosen4 = True
                  battleshipplayer2coords[battleshipcoordslist.index(inp)] = "O"
                  battleshipplayer2coords[battleshipcoordslist.index(inp) + 1] = "O"
                  battleshipplayer2coords[battleshipcoordslist.index(inp) + 2] = "O"
                else:
                  print("")
                  print("Invalid input, please try again")
              chosen4 = False
              battleshipplayer2print()
              print("")
def battleshipsetup(): #set up the board for player 1
              global chosen4
              global battleshipcoordslist
              global battleshipcoords
              print("")
              print("You have 4 battleships. 2 horizontal, 2 vertical, each have a 2-segment and 3-segment ship each.")
              print("")
              while chosen4 == False: #loops till valid input
                battleshipplayer1print()
                inp = input("Choose where the top segment of your vertical 2-segment ship will be on the grid: ").upper()
                if inp in battleshipcoordslist and "F" not in inp and battleshipcoords[battleshipcoordslist.index(inp)] != "O" and battleshipcoords[battleshipcoordslist.index(inp) + 6] != "O":
                  chosen4 = True
                  battleshipcoords[battleshipcoordslist.index(inp)] = "O"
                  battleshipcoords[battleshipcoordslist.index(inp) + 6] = "O"
                else:
                  print("")
                  print("Invalid input, please try again")
              chosen4 = False
              while chosen4 == False: #loops till valid input
                battleshipplayer1print()
                inp = input("Choose where the top segment of your vertical 3-segment ship will be on the grid: ").upper()
                if inp in battleshipcoordslist and "F" not in inp and "E" not in inp and battleshipcoords[battleshipcoordslist.index(inp)] != "O" and battleshipcoords[battleshipcoordslist.index(inp) + 6] != "O" and battleshipcoords[battleshipcoordslist.index(inp) + 12] != "O":
                  chosen4 = True
                  battleshipcoords[battleshipcoordslist.index(inp)] = "O"
                  battleshipcoords[battleshipcoordslist.index(inp) + 6] = "O"
                  battleshipcoords[battleshipcoordslist.index(inp) + 12] = "O"
                else:
                  print("")
                  print("Invalid input, please try again")
              chosen4 = False
              while chosen4 == False: #loops till valid input
                battleshipplayer1print()
                inp = input("Choose where the leftmost segment of your horizontal 2-segment ship will be on the grid: ").upper()
                if inp in battleshipcoordslist and "6" not in inp and battleshipcoords[battleshipcoordslist.index(inp)] != "O" and battleshipcoords[battleshipcoordslist.index(inp) + 1] != "O":
                  chosen4 = True
                  battleshipcoords[battleshipcoordslist.index(inp)] = "O"
                  battleshipcoords[battleshipcoordslist.index(inp) + 1] = "O"
                else:
                  print("")
                  print("Invalid input, please try again")
                  print("")
              chosen4 = False
              while chosen4 == False: #loops till valid input
                battleshipplayer1print()
                inp = input("Choose where the leftmost segment of your horizontal 3-segment ship will be on the grid: ").upper()
                if inp in battleshipcoordslist and "5" not in inp and "6" not in inp and battleshipcoords[battleshipcoordslist.index(inp)] != "O" and battleshipcoords[battleshipcoordslist.index(inp) + 1] != "O" and battleshipcoords[battleshipcoordslist.index(inp) + 2] != "O":
                  chosen4 = True
                  battleshipcoords[battleshipcoordslist.index(inp)] = "O"
                  battleshipcoords[battleshipcoordslist.index(inp) + 1] = "O"
                  battleshipcoords[battleshipcoordslist.index(inp) + 2] = "O"
                else:
                  print("")
                  print("Invalid input, please try again")
              chosen4 = False
              battleshipplayer1print()
              print("")
def battleshipbotsetup(): #set up the board for bot
              global battleshipcoordslist
              global battleshipplayer2coords
              global chosen4
              chosen4 = False
              while chosen4 == False: #loops till valid input
                inp = battleshipcoordslist[random.randint(0,(len(battleshipcoordslist) - 1))]
                if inp in battleshipcoordslist and "F" not in inp and battleshipplayer2coords[battleshipcoordslist.index(inp)] != "O" and battleshipplayer2coords[battleshipcoordslist.index(inp) + 6] != "O":
                  chosen4 = True
                  battleshipplayer2coords[battleshipcoordslist.index(inp)] = "O"
                  battleshipplayer2coords[battleshipcoordslist.index(inp) + 6] = "O"
              chosen4 = False
              while chosen4 == False: #loops till valid input
                inp = battleshipcoordslist[random.randint(0,(len(battleshipcoordslist) - 1))]
                if inp in battleshipcoordslist and "F" not in inp and "E" not in inp and battleshipplayer2coords[battleshipcoordslist.index(inp)] != "O" and battleshipplayer2coords[battleshipcoordslist.index(inp) + 6] != "O" and battleshipplayer2coords[battleshipcoordslist.index(inp) + 12] != "O":
                  chosen4 = True
                  battleshipplayer2coords[battleshipcoordslist.index(inp)] = "O"
                  battleshipplayer2coords[battleshipcoordslist.index(inp) + 6] = "O"
                  battleshipplayer2coords[battleshipcoordslist.index(inp) + 12] = "O"
              chosen4 = False
              while chosen4 == False: #loops till valid input
                inp = battleshipcoordslist[random.randint(0,(len(battleshipcoordslist) - 1))]
                if inp in battleshipcoordslist and "6" not in inp and battleshipplayer2coords[battleshipcoordslist.index(inp)] != "O" and battleshipplayer2coords[battleshipcoordslist.index(inp) + 1] != "O":
                  chosen4 = True
                  battleshipplayer2coords[battleshipcoordslist.index(inp)] = "O"
                  battleshipplayer2coords[battleshipcoordslist.index(inp) + 1] = "O"
              chosen4 = False
              while chosen4 == False: #loops till valid input
                inp = battleshipcoordslist[random.randint(0,(len(battleshipcoordslist) - 1))]
                if inp in battleshipcoordslist and "5" not in inp and "6" not in inp and battleshipplayer2coords[battleshipcoordslist.index(inp)] != "O" and battleshipplayer2coords[battleshipcoordslist.index(inp) + 1] != "O" and battleshipplayer2coords[battleshipcoordslist.index(inp) + 2] != "O":
                  chosen4 = True
                  battleshipplayer2coords[battleshipcoordslist.index(inp)] = "O"
                  battleshipplayer2coords[battleshipcoordslist.index(inp) + 1] = "O"
                  battleshipplayer2coords[battleshipcoordslist.index(inp) + 2] = "O"
              chosen4 = False
def battleshipplayer1blankprint(): #prints player 2's point of view of player 1's board
  global battleshipplayer1blank
  global battleshipcount
  battleshipcount = 0
  for c in battleshipplayer1blank:
                      battleshipcount += 1
                      if battleshipcount % 6 == 1:
                        print("")
                        print("|",c,"|", end = "")
                      else:
                        print("|",c,"|", end = "")
  print("")
  print("")
def battleshipplayer2blankprint(): #prints player 1's point of view of player s's board
  global battleshipplayer2blank
  global battleshipcount
  battleshipcount = 0
  for v in battleshipplayer2blank:
                      battleshipcount += 1
                      if battleshipcount % 6 == 1:
                        print("")
                        print("|",v,"|", end = "")
                      else:
                        print("|",v,"|", end = "")
  print("")
  print("")
def battleshippvpwincheck(): #checks for a winner for pvp battleship if someone has sunken all ships
  global battleshipplayer1blank
  global battleshipplayer2blank
  global battleshipcoords
  global battleshipend
  global battleshipwincount
  global battleshipplayer2wincount
  battleshipwincount = 0
  battleshipplayer2wincount = 0
  for n in battleshipplayer2blank:
    if n == "O":
      battleshipwincount += 1
  if battleshipwincount == 10:
    print("")
    print("Player 1 has hit down all of Player 2's ships! Player 1 wins!")
    battleshipend = True
  for m in battleshipplayer1blank:
    if m == "O":
      battleshipplayer2wincount += 1
  if battleshipplayer2wincount == 10:
    print("")
    print("Player 2 has hit down all of Player 1's ships! Player 2 wins!")
    battleshipend 
    battleshipend = True
def battleshipwincheck(): #checks for a winner for vs bot battleship if someone has sunken all ships
  global battleshipplayer1blank
  global battleshipplayer2blank
  global battleshipcoords
  global battleshipend
  global battleshipwincount
  global battleshipplayer2wincount
  battleshipwincount = 0
  battleshipplayer2wincount = 0
  for n in battleshipplayer2blank:
    if n == "O":
      battleshipwincount += 1
  if battleshipwincount == 10:
    print("")
    print("You have hit down all of the bot's ships! You win!")
    battleshipend = True
  for m in battleshipplayer1blank:
    if m == "O":
      battleshipplayer2wincount += 1
  if battleshipplayer2wincount == 10:
    print("")
    print("The bot has hit down all of your ships! The bot wins!")
    battleshipend 
    battleshipend = True
def tictactoeeasymodeplayer2(): #easy mode tictactoe, where bot chooses input at random and player 1 is playing as "O"
  global tictactoeend
  global playerturn
  global validbotinput
  global chosen5
  while tictactoeend == False: #loops till player wins or draw
                   if playerturn % 2 == 1 and playerturn < 10: #player turn
                      playerturn += 1
                      chosen5 = False
                      tictactoecount = 0
                      coordscount = 0
                      tictactoecount = 0
                      for w in tictactoecoords:
                        tictactoecount += 1
                        if tictactoecount % 3 == 1:
                          print("")
                          print("|",w,"|", end = "")
                        else:
                          print("|",w,"|", end = "")
                      print("")
                      for e in coordslist:
                        coordscount += 1
                        if coordscount % 3 == 1:
                          print("")
                          print("|",e,"|", end = "")
                        else:
                          print("|",e,"|", end = "")
                      print("")
                      print("")
                      tictactoewincheck()
                      print("")
                      while chosen5 == False: #loops till valid input
                        print("Player's turn")
                        print("")
                        inp = input("Enter the coordinate of the tile you would like to click here: ").upper()
                        if inp in coordslist and tictactoecoords[coordslist.index(inp)] == " ":
                          chosen5 = True
                          tictactoecoords[coordslist.index(inp)] = tictactoeplayer
                        else:
                          print("")
                          print("Invalid input! Please try again.")
                          print("")
                   elif playerturn == 10: #all nine squares done
                     tictactoeend = False
                     tictactoewincheck()
                     if tictactoeend == False:
                      print("")
                      print("Draw!")
                      tictactoeend = True
                   else: #bot turn
                     playerturn += 1
                     validbotinput = False
                     tictactoecount = 0
                     for w in tictactoecoords:
                      tictactoecount += 1
                      if tictactoecount % 3 == 1:
                        print("")
                        print("|",w,"|", end = "")
                      else:
                        print("|",w,"|", end = "")
                     print("")
                     print("")
                     tictactoewincheck()
                     while validbotinput == False: #loops till valid input
                      botgeneration = random.randint(0,8)
                      if tictactoecoords[botgeneration] == " ":
                        tictactoecoords[botgeneration] = tictactoebot
                        validbotinput = True
unscrambledexp = 0
hangmanexp = 0
battleshipexp = 0
tictactoeexp = 0
rockpaperscissorsexp = 0 #the exp that determines if you are at 'master' rank yet
unscrambledpro = False
hangmanpro = False
battleshippro = False
tictactoepro = False
rockpaperscissorspro = False #all the 'pro' conditions determine if the player has yet to be 'master' rank in the games
gamelist = ["Tic-Tac-Toe", "Battleship", "Rock Paper Scissors", "Hangman", "Unscramble", "Rulebook", "Exit game"] #list of games
endgame = False #game will loop until this is true, which is when player inputs exit game
while endgame == False: #game will loop until this is true, which is when player inputs exit game
  chosen = False
  chosen2 = False
  chosen3 = False
  chosen4 = False
  chosen5 = False
  chosen6 = False #'chosen' all ensure that the user inputs a valid input
  count = 0 
  tictactoecoords = [" "," "," "," "," "," "," "," "," "] #coordinates for tictactoe during game
  coordslist = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"] #coordinates for tictactoe
  tictactoecount = 0 #just used to print tictactoecoords in a 3x3 grid
  playerturn = 0 #to track which player's turn it is. e.g. if even, player 1, else, player 2
  coordscount = 0 #just used to print coordslist in a 3x3 grid
  rockpaperscissorsoptions = ["Rock","Paper","Scissors"] #options for RPS
  rockpaperscissorsplayer1score = 0 #Player 1's score to player 2
  rockpaperscissorsplayer2score = 0 #Player 2's score to player 1
  battleshipcoords = [" ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "] #coordinates for player 1's shipyard
  battleshipplayer2coords = [" ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "] #coordinates for player 2's shipyard
  battleshipplayer1blank = [" ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "] #coordinates for player 1's shipyard in player 2's pov during guessing stage
  battleshipplayer2blank = [" ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "," ", " "," "] #coordinates for player 2's shipyard in player 1's pov during guessing stage
  battleshipcoordslist = ["A1", "A2","A3","A4", "A5","A6","B1", "B2","B3","B4", "B5","B6","C1", "C2","C3","C4", "C5","C6","D1", "D2","D3","D4", "D5","D6","E1","E2", "E3","E4","E5", "E6","F1","F2", "F3","F4","F5", "F6"] #list ofvalid coordinates for battleship
  battleshipcount = 0 #used to print coordinates in a 6x6 grid
  battleshipwincount = 0 #to count how many ships player 1 has sunken
  battleshipplayer2wincount = 0 #to count how many ships player 1 has sunken
  wordguessed = False #to check if word has been guessed
  hangmanend = False #to check if game has ended
  battleshipend = False #to check if game has ended
  unscrambledend = False #to check if game has ended
  tictactoeend = False #to check if game has ended
  rockpaperscissorsend = False #to check if game has ended
  while chosen == False: #loops till valid input
    time.sleep(2)
    print("")
    print("Alright, please pick a game to play from these")
    print("options: ")
    print("")
    for game in gamelist:
      print(count + 1, end = "")
      print(".", end = " ")
      print(gamelist[count])
      count += 1
    count = 0
    print("")
    print("(if this is your first time or you do not recognise a game, click 6!)")
    print("")
    inp = input("Enter option number here: ")
    print("")
    if inp == "1":
      chosen = True
      print("Tic-Tac-Toe it is!")
      print("")
      print("Welcome to Tic-Tac-Toe! One of many iconic games in your personal mini arcade! Don't know how to play Tic-Tac-Toe? Here are the rules:")
      print("")
      print("            BASIC RULES:")
      print("")
      print("1. Players take turns putting their marks in empty squares. The player who has chosen 'X' will start first.")
      print("2. The first player to have 3 of their chosen shape IN A ROW (horizontally, vertically or diagonally) on the 3 by 3 board wins!")
      print("3. If all 9 squares on the 3 by 3 board are taken and no player has 3 shapes in a row, the game ends in a tie!")
      print("")
      while chosen2 == False: #loops till valid input
        print("1. Friend")
        print("2. Bot")
        print("")
        inp = input("Would you like to pass-n-play with a friend besides you or play against a bot? Input the number allocated to your choice: ")
        print("")
        if inp == "1":
          chosen2 = True
          print("You have chosen to play with a friend! Let's start! Remember to play fair and have fun! Please pass the device to player 1 to start the game.")
          print("")
          tictactoepvp()
          # pvp Tic-Tac-Toe
        elif inp == "2":
          chosen2 = True
          print("You have chosen to play with a bot!")
          while chosen3 == False: #loops till valid input
            print("1. Easy")
            print("2. Hard")
            print("")
            inp = input("Which difficulty will you want to play against? Pick the number allocated to your choice: ")
            print("")
            if inp == "1":
              print("You have chosen Easy Mode! Remember to have fun and happy playing!")
              print("")
              chosen3 = True
              tictactoeend = False
              while chosen4 == False: #loops till valid input
                print("1. 'X'")
                print("2. 'O'")
                print("")
                inp = input("Would you like to be 'X' or 'O'? Input the number corresponding to your choice: ")
                if inp == "1":
                  tictactoeplayer = "X"
                  tictactoebot = "O"
                  print("You have chosen to play as {}!".format(tictactoeplayer))
                  print("")
                  print("Let The Game Begin!")
                  chosen4 = True
                  playerturn = 0
                  tictactoeeasymode()
                elif inp == "2":
                  tictactoeplayer = "O"
                  tictactoebot = "X"
                  print("You have chosen to play as {}!".format(tictactoeplayer))
                  chosen4 = True
                  print("Let The Game Begin!")
                  playerturn = 1
                  tictactoeeasymodeplayer2()
                else:
                  print("Invalid choice! Please pick a  valid input.")
            elif inp == "2":
              print("You have chosen Hard Mode! Remember to have fun and happy playing!")
              chosen3 = True
              tictactoeend = False
              while chosen4 == False: #loops till valid input
                print("1. 'X'")
                print("2. 'O'")
                print("")
                inp = input("Would you like to be 'X' or 'O'? Input the number corresponding to your choice: ")
                if inp == "1":
                  tictactoeplayer = "X"
                  tictactoebot = "O"
                  print("You have chosen to play as {}!".format(tictactoeplayer))
                  print("")
                  print("Let The Game Begin!")
                  chosen4 = True
                  playerturn = 0
                  tictactoehardmode()
                elif inp == "2":
                  tictactoeplayer = "O"
                  tictactoebot = "X"
                  print("")
                  print("You have chosen to play as {}!".format(tictactoeplayer))
                  chosen4 = True
                  print("")
                  print("Let The Game Begin!")
                  playerturn = 1
                  tictactoehardmodeplayer2()
                else:
                  print("Invalid choice! Please pick a  valid input.")
            else:
              print("Invalid input! Please input a valid number.")
              print("")
        else:
          print("Invalid input! Please input a valid number.")
          print("")
      tictactoeexp += 100
      print("")
      print("You just gained 100 experience points for 'Tic-Tac-Toe'!")
      print("")
      if tictactoeexp >= 1000 and tictactoepro == False:
        print("You've mastered 'Tic-Tac-Toe'!")
        tictactoepro = True
    elif inp == "2":
      chosen = True
      print("Battleship it is!")
      print("")
      while chosen2 == False: #loops till valid input
        print("1. Friend")
        print("2. Bot")
        print("")
        inp = input("Would you like to pass-n-play with a friend besides you or play against a bot? Input the number allocated to your choice: ")
        print("")
        if inp == "1":
          chosen2 = True
          print("You have chosen to play with a friend! Let's start!")
          print("")
          print("Please pass the device to Player 1.")
          print("")
          battleshipsetup()
          for l in range(30): #clear screen
            print("")
          print("Please pass the device to Player 2")
          time.sleep(1)
          print("")
          battleshipplayer2setup()
          print("All proceedures done! Proceeding with game...")
          print("")
          for b in range(40): #clear screen
            print("")
          while battleshipend == False: #loops till player sinks all ships
            chosen5 = False
            if playerturn % 2 == 0:
              while chosen5 == False: #loops till valid input
                battleshipplayer2blankprint()
                print("")
                print("")
                battleshipprintcoordslist()
                inp = input("Player 1, please guess a corrdinate here: ").upper()
                print("")
                if inp in battleshipcoordslist and battleshipplayer2blank[battleshipcoordslist.index(inp)] == " ":
                  chosen5 = True
                  if battleshipplayer2coords[battleshipcoordslist.index(inp)] == "O":
                    battleshipplayer2blank[battleshipcoordslist.index(inp)] = "O"
                    print("You hit a ship!")
                    print("")
                  else:
                    battleshipplayer2blank[battleshipcoordslist.index(inp)] = "X"
                    print("You did not hit a ship!")
                    print("")
                else:
                  print("Invalid input! Please try again.")
              battleshipplayer2blankprint()
              print("")
              print("Above is Player 2's board after your input. Please pass the device to Player 2.")
              time.sleep(2)
            else:
              while chosen5 == False: #loops till valid input
                battleshipplayer1blankprint()
                print("")
                print("")
                battleshipprintcoordslist()
                inp = input("Player 2, please guess a corrdinate here: ").upper()
                print("")
                if inp in battleshipcoordslist and battleshipplayer1blank[battleshipcoordslist.index(inp)] == " ":
                  chosen5 = True
                  if battleshipcoords[battleshipcoordslist.index(inp)] == "O":
                    battleshipplayer1blank[battleshipcoordslist.index(inp)] = "O"
                    print("You hit a ship!")
                    print("")
                  else:
                    battleshipplayer1blank[battleshipcoordslist.index(inp)] = "X"
                    print("You did not hit a ship!")
                    print("")
                else:
                  print("Invalid input! Please try again.")
                  print("")
              battleshipplayer1blankprint()
              print("")
              print("Above is Player 1's board after your input. Please pass the device to Player 1.")
              time.sleep(1)
            playerturn += 1
            battleshippvpwincheck()
          #pvp battleship
        elif inp == "2": #bot battleship
          chosen2 = True
          print("You have chosen to play with a bot!")
          print("")
          battleshipsetup()
          print("")
          print("Wait one moment...")
          print("")
          battleshipbotsetup()
          while battleshipend == False: #loops till a player sinks all ships
            chosen5  = False
            if playerturn % 2 == 0:
              while chosen5 == False: #loops till valid input
                battleshipplayer2blankprint()
                print("")
                print("")
                battleshipprintcoordslist()
                inp = input("Please guess a corrdinate here: ").upper()
                print("")
                if inp in battleshipcoordslist and battleshipplayer2blank[battleshipcoordslist.index(inp)] == " ":
                  chosen5 = True
                  if battleshipplayer2coords[battleshipcoordslist.index(inp)] == "O":
                    battleshipplayer2blank[battleshipcoordslist.index(inp)] = "O"
                    print("You hit a ship!")
                    print("")
                  else:
                    battleshipplayer2blank[battleshipcoordslist.index(inp)] = "X"
                    print("You did not hit a ship!")
                    print("")
                else:
                  print("Invalid input! Please try again.")
              battleshipplayer2blankprint()
              print("")
              print("Above is the bot's board after your input.")
              time.sleep(2)
            else:
              while chosen5 == False: #loops till valid input
                inp = battleshipcoordslist[random.randint(0, (len(battleshipcoordslist) - 1))]
                print("")
                if inp in battleshipcoordslist and battleshipplayer1blank[battleshipcoordslist.index(inp)] == " ":
                  chosen5 = True
                  if battleshipcoords[battleshipcoordslist.index(inp)] == "O":
                    battleshipplayer1blank[battleshipcoordslist.index(inp)] = "O"
                    print("Bot hits a ship!")
                    print("")
                  else:
                    battleshipplayer1blank[battleshipcoordslist.index(inp)] = "X"
                    print("Bot did not hit a ship!")
                    print("")
              battleshipplayer1blankprint()
              print("")
              print("Above is your board after the bot's input.")
              time.sleep(1)
            playerturn += 1
            battleshipwincheck()
      battleshipexp += 100
      print("")
      print("You just gained 100 experience points for 'Battleship'!")
      print("")
      if battleshipexp >= 1000 and battleshippro == False:
        print("You've mastered 'Battleship'!")
        battleshippro = True
    elif inp == "3":
      chosen = True
      print("Rock Paper Scissors it is!")
      print("")
      while chosen2 == False: #loops till valid input
        print("1. Friend")
        print("2. Bot")
        print("")
        inp = input("Would you like to pass-n-play with a friend besides you or play against a bot? Input the number allocated to your choice: ")
        print("")
        if inp == "1":
          chosen2 = True
          print("You have chosen to play with a friend! Let's start!")
          while rockpaperscissorsend == False: #loops till player chooses to stop playing again
            chosen3 = False
            chosen4 = False
            chosen5 = False
            count = 0
            print("")
            while chosen3 == False: #loops till valid input
              for t in rockpaperscissorsoptions:
                count += 1
                print(count, end = "")
                print(".", t)
              print("")
              inp = input("Player 1, pick the number allocated to your choice: ")
              if inp == "1":
                rockpaperscissorsplayer1 = rockpaperscissorsoptions[int(inp) - 1]
                chosen3 = True
              elif inp == "2":
                rockpaperscissorsplayer1 = rockpaperscissorsoptions[int(inp) - 1]
                chosen3 = True
              elif inp == "3":
                rockpaperscissorsplayer1 = rockpaperscissorsoptions[int(inp) - 1]
                chosen3 = True
              else:
                print("Invalid input, please try again.")
              count = 0
            for y in range(30): #clear screen
              print("")
            time.sleep(1)
            print("Please pass the device to Player 2 now")
            print("")
            time.sleep(1)
            while chosen4 == False: #loops till valid input
              for t in rockpaperscissorsoptions:
                count += 1
                print(count, end = "")
                print(".", t)
              print("")
              inp = input("Player 2, pick the number allocated to your choice: ")
              if inp == "1":
                rockpaperscissorsplayer2 = rockpaperscissorsoptions[int(inp) - 1]
                chosen4 = True
              elif inp == "2":
                rockpaperscissorsplayer2 = rockpaperscissorsoptions[int(inp) - 1]
                chosen4 = True
              elif inp == "3":
                rockpaperscissorsplayer2 = rockpaperscissorsoptions[int(inp) - 1]
                chosen4 = True
              else:
                print("Invalid input, please try again.")
            for y in range(30): #clear screen
              print("")
            print("Rock!")
            time.sleep(1)
            print("")
            print("Paper!")
            time.sleep(1)
            print("")
            print("Scissors!")
            time.sleep(1)
            print("")
            print("SHOOT!")
            time.sleep(0.5)
            print("")
            rockpaperscissorswincheck()
            print("")
            print("The scores are:")
            print("")
            print("Player 1 - Player 2")
            print(rockpaperscissorsplayer1score,"-", rockpaperscissorsplayer2score)
            while chosen5 == False: #loops till valid input
              print("")
              print("1. Yes")
              print("2. No")
              print("")
              inp = input("Do you want to play again: ")
              if inp == "1":
                print("")
                print("Great! Please pass the device to player 1 and continue.")
                chosen5 = True
              elif inp == "2":
                print("")
                if rockpaperscissorsplayer1score > rockpaperscissorsplayer2score:
                  print("Player 1 wins overall!")
                elif rockpaperscissorsplayer1score < rockpaperscissorsplayer2score:
                  print("Player 2 wins overall!")
                else:
                  print("In the end, everyone wins! It's a draw overall.")
                rockpaperscissorsend = True
                chosen5 = True
              else:
                print("")
                print("Invalid input, please try again.")
        elif inp == "2":
          chosen2 = True
          print("You have chosen to play with a bot!")
          rockpaperscissorsend = False
          while rockpaperscissorsend == False: #loops till player stops playing again
            chosen3 = False
            chosen4 = False
            chosen5 = False
            count = 0
            print("")
            while chosen3 == False: #loops till valid input
              for t in rockpaperscissorsoptions:
                count += 1
                print(count, end = "")
                print(".", t)
              print("")
              inp = input("Player 1, pick the number allocated to your choice: ")
              if inp == "1":
                rockpaperscissorsplayer1 = rockpaperscissorsoptions[int(inp) - 1]
                chosen3 = True
              elif inp == "2":
                rockpaperscissorsplayer1 = rockpaperscissorsoptions[int(inp) - 1]
                chosen3 = True
              elif inp == "3":
                rockpaperscissorsplayer1 = rockpaperscissorsoptions[int(inp) - 1]
                chosen3 = True
              else:
                print("Invalid input, please try again.")
              count = 0
            for y in range(30): #clear screen
              print("")
              inp = str(random.randint(1,3))
              if inp == "1":
                rockpaperscissorsplayer2 = rockpaperscissorsoptions[int(inp) - 1]
                chosen4 = True
              elif inp == "2":
                rockpaperscissorsplayer2 = rockpaperscissorsoptions[int(inp) - 1]
                chosen4 = True
              elif inp == "3":
                rockpaperscissorsplayer2 = rockpaperscissorsoptions[int(inp) - 1]
                chosen4 = True
            print("Rock!")
            time.sleep(1)
            print("")
            print("Paper!")
            time.sleep(1)
            print("")
            print("Scissors!")
            time.sleep(1)
            print("")
            print("SHOOT!")
            time.sleep(0.5)
            print("")
            rockpaperscissorswincheck()
            print("")
            print("The scores are:")
            print("")
            print("Player 1 - Bot")
            print(rockpaperscissorsplayer1score,"-", rockpaperscissorsplayer2score)
            while chosen5 == False: #loops till valid input
              print("")
              print("1. Yes")
              print("2. No")
              print("")
              inp = input("Do you want to play again: ")
              if inp == "1":
                print("")
                print("Great! Have fun!")
                chosen5 = True
              elif inp == "2":
                print("")
                if rockpaperscissorsplayer1score > rockpaperscissorsplayer2score:
                  print("Player 1 wins overall!")
                elif rockpaperscissorsplayer1score < rockpaperscissorsplayer2score:
                  print("Bot wins overall!")
                else:
                  print("In the end, everyone wins! It's a draw overall.")
                rockpaperscissorsend = True
                chosen5 = True
              else:
                print("")
                print("Invalid input, please try again.")
          # bot rock paper scissors here
        else:
          print("Invalid input! Please input a valid number.")
          print("")
      rockpaperscissorsexp += 100
      print("")
      print("You just gained 100 experience points for 'Rock Paper Scissors'!")
      print("")
      if rockpaperscissorsexp >= 1000 and rockpaperscissorspro == False:
        print("")
        print("You've mastered 'Rock Paper Scissors'!")
        rockpaperscissorspro = True
        print("")
    elif inp == "4":
      chosen = True
      print("Hangman it is!")
      print("")
      print("Please pass the device to player 1.")
      time.sleep(1)
      while chosen2 == False: #loops till valid word
        print("")
        word = input("Player 2 trusts you to enter a valid word. Please enter a valid word for Player 2 to guess: ").lower()
        chosen2 = True
        if word != "" and " " not in word:
          for u in word:
            if not u.lower().isalpha():
              chosen2 = False
              print("")
              print("Invalid input detected! Please only input alphabets")
        else:
          chosen2 = False
          print("")
          print("Invalid input detected! Please only input alphabets")
        print("")
        print("")
        category = input("Player 2 trusts you to enter a valid category. Please enter a valid category for Player 2: ")
      while chosen4 == False: #loops till valid input
        print("")
        hangmanlives = input("Enter the number of lives you want Player 2 to have: ")
        print("")
        if hangmanlives.isdigit(): #checks if input is only integer
          chosen4 = True
        else:
          print("Invalid input! Please try again.")
      chosen4 = False 
      while chosen4 ==  False: #loops till valid input
        print("")
        hangmanhints = input("Enter the number of hints you want Player 2 to have: ")
        print("")
        if hangmanhints.isdigit(): #checks if input is integer
          if int(hangmanhints) < len(word): #checks if input is less than number of letters
            chosen4 = True
          else:
            print("You cannot have the same number or more hints than letters in your word! Please try again.")
        else:
          print("Invalid input! Please try again.")
      for p in range(40): #clear screen
        print("")
      print("Please pass the device to player 2 now.")
      time.sleep(1)
      print("")
      print("Game Start!")
      print("")
      wordlist = [*word]
      foundwords = []
      for s in wordlist:
        foundwords.append("_")
      while hangmanend == False: #loop till player guesses word or runs out of lives
        chosen5 = False
        count = 0
        if int(hangmanlives) == 0: #no lives left
          print("")
          print("You have run out of lives! The answer was", word)
          hangmanend = True
        elif wordguessed == True: #word has been guessed correctly
          print("")
          print("Congratulations, you win! The answer was", word)
          hangmanend = True
        elif foundwords == wordlist: #all letters have been guessed
          for f in foundwords:
            print(f, end = " ")
          print("")
          print("")
          print("Congratulations, you win! The answer was", word)
          hangmanend = True
        else:
          while chosen5 == False: #loops till valid input
            for a in foundwords:
              print(a, end = " ")
            print("")
            print("")
            print("Catgory:", category)
            print("")
            print("You have {} lives left.".format(hangmanlives))
            print("")
            print("1. Guess the word")
            print("2. Guess a letter")
            print("3. Get a hint! You have {} hint(s) left.".format(hangmanhints))
            print("")
            inp = input("Would you like the guess the word or guess a letter? Pick the number allocated to your choice: ")
            print("")
            if inp == "1":
              chosen5 = True
              print("")
              inp = input("Alright, please type in your word here: ")
              print("")
              if inp.lower() == word.lower():
                wordguessed = True #win
              else:
                print("Incorrect!")
                hangmanlives = int(hangmanlives) - 1 #wrong
              #guess word
            elif inp == "2":
              chosen5 = True
              inp = input("Alright, please type in your letter that you want to guess here: ")
              print("")
              if inp == "":
                print("You didn't guess a letter? Incorrect!")
                hangmanlives = int(hangmanlives) - 1
                #no mercy
              elif len(inp) != 1:
                print("You tried to submit more than 1 letter? Incorrect!")
                hangmanlives = int(hangmanlives) - 1
                #no mercy
              elif inp.lower() in word.lower():
                for g in word.lower():
                  if g == inp.lower():
                    foundwords[count] = wordlist[count]
                    count += 1
                  else:
                    count += 1
                #update hangman word
              else:
                print("Incorrect!")
                hangmanlives = int(hangmanlives) - 1
                #wrong letter
              print("")
            elif inp == "3":
              if int(hangmanhints) > 0:
                hangmanhints = int(hangmanhints) - 1
                chosen6 = False
                while chosen6 == False: #loops till valid input
                  hangmanrandom = random.randint(0, (len(wordlist)-1))
                  if foundwords[hangmanrandom] == "_":
                    foundwords[hangmanrandom] = wordlist[hangmanrandom]
                    chosen6 = True
                print("")
                print("Hint given!")
                print("")
              else:
                print("")
                print("You have no hints left! Please input 1 or 2")
            else:
              print("Invalid input! Please try again.")
      # pvp hangman
      hangmanexp += 100
      print("")
      print("You just gained 100 experience points for 'Hangman'!")
      print("")
      if hangmanexp >= 1000 and hangmanpro == False:
        print("")
        print("You've mastered 'Hangman'!")
        hangmanpro = True
        print("")
    elif inp == "5":
      chosen = True
      while chosen2 == False: #loops till valid input
        print("")
        unscrambledword = input("Player 2 trusts you to enter a valid word. Please enter a valid word for Player 2 to guess: ").lower()
        chosen2 = True
        if unscrambledword != "" and " " not in unscrambledword and len(unscrambledword) > 1: #checks if input is more than 1 letter
          for u in unscrambledword:
            if not u.lower().isalpha():
              chosen2 = False
              print("")
              print("Invalid input detected! Please only input alphabets")
        else:
          chosen2 = False
          print("")
          print("Invalid input detected! Please only input alphabets and include more than 1 letter.")
        print("")
      print("")
      unscrambledcategory = input("Player 2 trusts you to enter a valid category. Please enter a valid category for Player 2: ")
      while chosen4 == False: #loops till valid input
        print("")
        unscrambledlives = input("Enter the number of lives you want Player 2 to have: ")
        print("")
        if unscrambledlives.isdigit(): #checks if input is integer
          chosen4 = True
        else:
          print("Invalid input! Please try again.")
      chosen4 = False
      while chosen4 == False: #loops till valid input
        print("")
        unscrambledhints = input("Enter the number of hints you want Player 2 to have: ")
        print("")
        if unscrambledhints.isdigit(): #checks if input is integer
          if int(unscrambledhints) < (len(unscrambledword)): #checks if input is more than number of letters
            chosen4 = True
          else:
            print("You cannot have the same amount or more hints than letters in your word. Please try again.")
        else:
          print("Invalid input! Please try again.")
      unscrambledwordlist = [*unscrambledword]
      scrambledwordlist = unscrambledwordlist.copy()
      random.shuffle(scrambledwordlist)
      while scrambledwordlist == unscrambledwordlist: #shuffles till different order
        random.shuffle(scrambledwordlist)
      unscrambledhintlist = []
      for q in scrambledwordlist:
        unscrambledhintlist.append("_")
      for p in range(40): #clear screen
        print("")
      print("Please pass the device to Player 2 now.")
      time.sleep(1)
      print("")
      print("Game Start!")
      print("")
      while unscrambledend == False: #loops till player runs out of lives or guesses word
            print("")
            for a in scrambledwordlist:
              print(a, end = " ")
            print("")
            print("")
            for b in unscrambledhintlist:
              print(b, end = " ")
            print("")
            print("")
            print("Catgory:", unscrambledcategory)
            print("")
            print("You have {} lives left.".format(unscrambledlives))
            print("")
            print("1. Guess the word")
            print("2. Get a hint! You have {} hint(s) left.".format(unscrambledhints))
            print("")
            inp = input("Would you like the guess the word or guess a letter? Pick the number allocated to your choice: ")
            print("")
            if inp == "1": #guess word
              inp = input("Alright! Input your word here: ")
              print("")
              if inp == unscrambledword: #correct
                print("Player 2 wins! Congratulations!")
                unscrambledend = True
              else: #wrong
                unscrambledlives = int(unscrambledlives) - 1
                print("Incorrect!")
              print("")
            elif inp == "2" and int(unscrambledhints) > 0: #hint
              unscrambledhints = int(unscrambledhints) - 1
              chosen6 = False
              while chosen6 == False: #loops till valid hint given
                unscrambledrandom = random.randint(0, (len(scrambledwordlist) - 1))
                if unscrambledhintlist[unscrambledrandom] == "_":
                  unscrambledhintlist[unscrambledrandom] = unscrambledwordlist[unscrambledrandom]
                  chosen6 = True
              if int(unscrambledlives) < 1: #checks if player ran out of lives
                print("")
                print("Player 2 has run out of lives, Player 1 wins!")
                print("")
                unscrambledend = True
            else:
              print("Invalid input! Please try again.")
              print("")
      unscrambledexp += 100
      print("")
      print("You just gained 100 experience points for 'Unscrambled'!")
      print("")
      if unscrambledexp >= 1000 and unscrambledpro == False: #checks if reached rank
        print("")
        print("You've mastered 'Unscrambled!'")
        unscrambledpro = True
        print("")
    elif inp == "6": #rulebook
      print("1. TIC-TAC-TOE RULES:")
      print("")
      print("")
      print("What is Tic-Tac-Toe? Tic-Tac-Toe is a classic two-player game played on a 3x3 grid. The objective is to be the first player to form a line of three of their symbols (X or O) in a horizontal, vertical, or diagonal row.")
      print("The game is played between two players, one representing X and the other representing O, with the player choosing 'X' to start first.")
      print("Players take turns placing their symbol (X or O) on an empty cell within the grid during their respective turns.")
      print(" The game continues until one of the following happens:")
      print("")
      print("a. A player wins the game by getting three in a row.")
      print("b. The grid is completely filled with symbols, resulting in a tie/draw.")
      print("")
      print("What are you waiting for? Try it out!")
      print("")
      print("")
      print("")
      print("2. BATTLESHIP RULES:")
      print("")
      print("")
      print("What is Battleship? Battleship is a two-player strategy board game that simulates naval warfare. Each player has their own grid on which they place ships, and they take turns trying to guess the location of their opponent's ships.")
      print("The game is played between two players.")
      print("To start, players position their ships on their own ocean grid without showing the other player.")
      print("The rule is that ships cannot overlap or be placed partially off the grid.")
      print("Objective: The player who sinks all of their opponent's ships first by correctly guessing the coordinates wins the game.")
      print("")
      print("Got it? Now go try it out for yourself!")
      print("")
      print("")
      print("")
      print("3. ROCK PAPER SCISSORS RULES:")
      print("")
      print("")
      print("What is Rock-Paper-Scissors? Rock-Paper-Scissors is a simple hand game typically played between two people, where each player simultaneously forms one of three shapes with their hand.")
      print("Then how do you determine which shape wins?")
      print("")
      print("a. Rock crushes scissors (Rock wins against Scissors) ")
      print("b. Scissors cut paper (Scissors win against Paper).")
      print("c. Paper covers rock (Paper wins against Rock).")
      print("")
      print("Seems simple, but fun! Go try it now!")
      print("")
      print("")
      print("")
      print("4. HANGMAN RULES:")
      print("")
      print("")
      print("What is Hangman? Hangman is a word-guessing game where one player thinks of a word, and the other player tries to guess the letters in that word.")
      print("Player 1 thinks of a word and suitable category to input for Player 2 to use to guess. Player 1 also provides a suitable number of lives and hints for the player. A hint Provides 1 random word in the correct place for Player 2, but remember, there still could be more of that letter in the word!")
      print("")
      print("Player 2 then uses the provided category and number of letters to try and guess the word. The  player can guess a letter from the word. If correct, all occurences of that letter will reveal themself at the right positions, if incorrect, player loses a life. Attempting but failing to guess the word also removes a life from the player.")
      print("")
      print("If Player 2 is unable to guess the word in the set amount of lives, Player 1 wins! Likewise for vice-versa.")
      print("")
      print("Understood? Now try it out!")
      print("")
      print("")
      print("")
      print("5. UNSCRAMBLE RULES:")
      print("")
      print("")
      print("What is Unscramble? Similar to Hangman, Unscramble is a word-guessing game where one player thinks of a word, and the other player tries to guess that word.")
      print("Player 1 thinks of a word and suitable category to input for Player 2 to use to guess. Player 1 also provides a suitable number of lives and hints for the player. A hint Provides 1 random word in the correct place for Player 2, but remember, there still could be more of that letter in the word!")
      print("")
      print("Player 2 then uses the provided category and number of letters to try and guess the word. Unlike in Hangman, Player 2 is unable to guess any letters. The letters are all provided to Player 2 in a random order, and it is Player 2's job to guess the word from the jumbled mess. ")
      print("")
      print("If Player 2 is unable to guess the word in the set amount of lives, Player 1 wins! Likewise for vice-versa.")
      print("")
      print("Youre all caught up! Give it a shot!")
      print("")
      print("")
      print("Thats all of the rules!")
      chosen = True
    elif inp == "7": #leave game
      print("Okay, byebye! Come back soon ! ^-^ !")
      chosen = True
      endgame = True
    else: #invalid input
      print("")
      print("Invalid input! Please input a valid number.")
      print("")