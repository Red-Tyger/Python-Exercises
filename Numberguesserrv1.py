#Rewrite of an example program in one of my Python books
import os, random

def setHeader(currentscore):
	"""prints a screen header at the start of each new game"""
	os.system("cls") #currently only works on NT systems
	print()
	print(" ########################################")
	print(" #                                      #")
	print(" #      The Guess My Number Game        #")
	print(" #                                      #")
	print(" #    So numbers. Much Guesses. Wow.    #")
	print(" #                                      #")
	print(" ########################################")
	print()
	print("      Played: " + str(currentscore[0]) + " Won: " + str(currentscore[1]) + " Lost: " + str(currentscore[2]))
	print()
	
def getPlayerName():
	"""gets player name, no special checks on user input at this time"""
	thisplayer = input(" What is your name? > ")
	thisplayer = thisplayer.title()
	print(" Hello, " + thisplayer + "!")
	return(thisplayer)
	
def pickRandom():
	"""generates a random integer between 1 and 20"""
	selectnum = random.randint(1,20)
	return(selectnum)

def checkGuess(targetnum):
	"""compares a player's guesses against the secret number selected by the computer"""
	guesscounter = 1 #initialize guess counter
	winner = False #set the win round to False, change to True if player wins
	while guesscounter <= 6:
		print(" Guess number " + str(guesscounter))
		guessinput = input(" Please guess a number between 1 and 20. > ")
		playerguess = numCheck(guessinput) #convert player input to an integer
		if playerguess == targetnum:
			print(" You guessed the number in " + str(guesscounter) + " guesses!")
			winner = True #reports a player win
			return(winner)
		elif playerguess < targetnum:
			print(" Your guess is too low.")
			guesscounter += 1
			#print("Guess Counter = " + str(guesscounter)) #debug line
		else:
			print(" Your guess is too high.")
			guesscounter += 1
			#print("Guess Counter = " + str(guesscounter)) #debug line
	print(" Sorry, the number I was thinking of was " + str(targetnum) + ".")
	#loopcondition = False #set condition to exit the while loop
	return(winner)

def numCheck(playerinput):
	"""Check player guess input to confirm it is a valid entry. Returns an integer value converted from string input if valid."""

	badentry = True #assume that the input is bad, until it passes the tests
	
	while badentry == True: #keep looping until BOTH the player input can be converted to an integer, and the integer is in range
		badinteger = True #assume that user has entered a non-integer, until it passes a test

		#validate user input
		while badinteger == True:
			try:
				playerinteger = int(playerinput) #still need to handle errors where input can't be converted to integers
				badinteger = False
				continue	
			except:
				print(" Not a valid integer.")
			playerinput = input(" Please enter a valid integer as a guess. >")
			
		print(playerinteger)
		if playerinteger >=1 and playerinteger <=20:
			badentry = False
			continue	
		elif playerinteger < 1:
			print(" You must enter a number equal to or greater than 1.")
		else:
			print(" You must enter a number less than or equal to 20.")

		playerinput = input(" Number is out of range, please re-enter your guess. > ")
				
	return(playerinteger)		

def gameRound(updatemyscore, contestant):
	"""collects the player guesses in the game"""
	updatemyscore[0] += 1 #update the round counter
	compsecret=pickRandom() #generate a random number
	print()
	print(" " + contestant + ", I have chosen a number between 1 and 20. You have 6 guesses to figure out what it is!")
	print()
	roundresult=checkGuess(compsecret) #play a round and determine if player wins
	if roundresult == True:
		updatemyscore[1] += 1 #update won counter
	else:
		updatemyscore[2] +=1 #update lost counter
	return(updatemyscore)
	
def playItAgain():
	"""Returns False condition for the quit main loop function, True if the player wishes to exit."""
	anothergame = False #initialize the play again input loop
	while anothergame == False:
		playerinput = input(" Would you like to play again (y/n)? > ") 
		playerinput = playerinput.lower()
		if playerinput == "yes":
			return False
		elif playerinput == "y":
			return False
		elif playerinput == "no":
			return True
		elif playerinput == "n":
			return True
		else:
			print()
			print(" I don't understand what you mean by " + playerinput + ".")
			playerinput = input(" Would you like to play again (y/n)? > ")

def mainGame():
	"""set up the main loop of the number guessing game"""
	#initialize main game loop quit condition to False, reset game scoreboard, present the opening game screen
	quitgame=False 
	scoreboard = [0,0,0] #list of games played, games won, games lost

	setHeader(scoreboard)	
	playername=getPlayerName()
	
	while quitgame == False:
		scoreboard=gameRound(scoreboard, playername) #play a round of the number guessing game
		quitgame = playItAgain() #ask if the player wants to play again, set quitgame to True if they do not
		setHeader(scoreboard)
	print(" " + playername + ", you played " + str(scoreboard[0]) + " games, you won " + str(scoreboard[1]) + " games and lost " + str(scoreboard[2]) + ".")

#test and debug after this line

mainGame()

#Other notes
#I think I want to include a function that will check the OS environment the program is running in, plus it might be fun to 
#pull the user's login name as a default name, with the option to chose a more casual address if the player prefers.
#The error checking section of the program was a bear, but we got it to work, finally. Key was the continue statement to force the loop back to the 
#top of the while statement.
