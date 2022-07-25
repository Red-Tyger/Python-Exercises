#more fun with dictionaries, trying to figure out how they work!

import os, time

def cltm():
	"""checks environment script is running in and issues appropriate command to OS to clear the terminal"""
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
		
def addItem(thedictionary):
	"""collects a key and a value to add to a dictionary. Disallows overwriting existing dictionary items: user will have to explicity direct the program to
	replace / overwrite a value for a key with chgItem in this application. Function only adds strings, no type conversion."""
	
	print("##### ADD ITEM #####\n")
	print("Current contents of dictionary: " + str(thedictionary))
	print()
	newkey = input("Please enter new KEY - >>> ")
	#error handling here to check if the entry for newkey will overwrite an existing key in the dictionary
	if newkey in thedictionary.keys():
		print("\nERROR - > " + newkey + " already exists, overwrite not permitted by this function. Operation cancelled.")
		time.sleep(2.5)
	else:
		newvalue = input("Please enter new VALUE - >>> ")
		print()
		commit=input("Do you wish to commit KEY " + newkey + " with VALUE " + newvalue + "? (y to commit) - >>> ")
		if commit == 'y':
			thedictionary[newkey] = newvalue
			print()
			print(thedictionary)
		else:
			print()
			print("Operation cancelled.")
			time.sleep(2)

def remItem(thedictionary):
	"""asks for a key to remove from the dictionary, checks to make sure that the indicated key is in the
	dictionary and returns an error if it is not."""
	
	print("##### REMOVE KEY #####\n")
	print("Current contents of dictionary: " + str(thedictionary))
	print()
	remkey = input("Please enter the key you want to remove >>>> ")
	if remkey in thedictionary.keys():
		chekremove = input("Remove KEY " + str(remkey) + "with VALUE " + str(thedictionary[remkey]) + " from dictionary? (y to commit) >>>> ")
		if chekremove == "y":
			del thedictionary[remkey]
		else:
			print("Operation cancelled.")
			time.sleep(2)
	else: #executes if the entered key is NOT in the current dictionary
		print("ERROR -> " + remkey + " not found in dictionary.")
		time.sleep(2)
		
def chgItem(thedictionary):
	"""asks for user to select an existing key to change its corresponding value."""
	
	print("##### MODIFY VALUE #####\n")
	print("Current contents of dictionary: " + str(thedictionary))
	print()
	chgkey = input("Please enter the key you want to modify >>>> ")
	if chgkey in thedictionary.keys():
		newvalue = input("Please enter new VALUE for KEY " + str(chgkey) + " >>>> ")
		chekchange = input("Change KEY " + str(chgkey) + "with VALUE " + str(thedictionary[chgkey]) + " to NEW VALUE " + newvalue + "? (y to commit) >>>> ")
		if chekchange == "y":
			thedictionary[chgkey] = newvalue
		else:
			print("Operation cancelled.")
			time.sleep(2)	
	else: #executes if the entered key is NOT in the current dictionary
		print("ERROR -> " + chgkey + " not found in dictionary.")
		time.sleep(2)

def scrubData(thedictionary):
	"""similar to remItem, but allows the user to select an index value for dictionary entries that are difficult to type accurately, such as misspelled or
	garbage key values"""
	
	keylist = []
	cltm()
	print("##### SCRUB BAD KEYS #####\n")
	print("Please use with caution!")
	
	#gather all keys in the dictionary
	for x in thedictionary.keys():
		keylist.append(x)

	print(keylist) #debug line
	print(len(keylist)) #debug line
	menudictionary = {} #initialize an empty dictionary that will associate numberic values with values associated with keys in the main dictionary
	myindex = 1 #initializes a human-intuitive index counter the user can use to refer to difficult to type entries
	for y in keylist:
		menudictionary[myindex] = y
		print(str(myindex) + ") KEY -> " + y + " ... VALUE -> " + thedictionary[y])
		myindex += 1 #increment the human-intuitvie index counter
	print(menudictionary) #debug line
		
	errorloop = True
	while errorloop == True:
		scrubitem = input("Select index number of dictionary item you wish to remove, enter 0 to cancel. >>>> ")
		
		try:
			valuecheck = int(scrubitem)
		except:
			print("ERROR - > " + scrubitem + " is not a valid entry!")
			print("Operation cancelled")
			time.sleep(2)
			continue
			
		if int(scrubitem) == 0:
			print("Operation cancelled by user.")
			errorloop = False
			time.sleep(2)
			continue	
		elif int(scrubitem) in menudictionary.keys():
			chekscrubremove = input("Remove KEY " + menudictionary[int(scrubitem)] + " from dictionary? (y to commit) >>>> ")
			if chekscrubremove == "y":
				del thedictionary[menudictionary[int(scrubitem)]]
				errorloop = False
				continue
			else:
				print("Operation cancelled.")
				time.sleep(2)
		else: #executes if the entered key is NOT in the current dictionary
			print("ERROR -> " + str(scrubitem) + " not an item in dictionary.")
			time.sleep(2)
	

def main():
	"""main loop of dictionary edit program"""
	
	keeploop = True #initialize the looping condition for the main while loop
	julyvalues = {} #initialize an empty dictionary!
	julyvalues = {"pet":"cat","food":"Fancy Feast","dddfae":"554wwwt"} #debug line to analyse function scrubData
	while keeploop:
		
		cltm() #custom terminal clear command!
		dictionarysize = len(julyvalues)
		print()
		print("This instance running on " + os.name)
		print("Current item count in dictionary: " + str(len(julyvalues)))
		print("Contents of dictionary: " + str(julyvalues))
		print()
		print("########### Menu Options ###########\n") #Kaze wanted me to put a newline characters in instead of empty print functions. Happy now, Kaze? XD
		print("     1 - Add ITEM to dictionary")
		print("     2 - Remove ITEM from dictionary")
		print("     3 - Modify KEY value")
		print("     q - Quit program\n")
		print("####################################")
		print("\n* Enter 'scrub' to review and remove bad KEYS from dictionary.*\n")
		myaction = input("Please choose an action from the menu. - >>> ")
		print()
		if myaction == 'q':
			keeploop = False
		elif myaction == "1":
			addItem(julyvalues)
		elif myaction == "2" and dictionarysize > 0:
			remItem(julyvalues)
		elif myaction == "3"and dictionarysize > 0:
			chgItem(julyvalues)
		elif myaction == "scrub" and dictionarysize > 0:
			scrubData(julyvalues)
		else:
			print("Invalid input error.")
			if dictionarysize == 0:
				print("ERROR -> Dictionary is Empty, no items to remove or modify.")
			time.sleep(2.5)
		print()
		
	print("Final contents of the dictionary: " + str(julyvalues))
	print("Program exit.")


#code excecution below this line.

main()
