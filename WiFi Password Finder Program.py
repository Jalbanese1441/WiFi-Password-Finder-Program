import os
import os.path # Necessary for me to work with file structures
import time #This lets me add in sleep commands 
cls = lambda: os.system("cls") #This allows me to clear the console

def setUp(networks): # This will set up the program by grabbing all of the network names
	file=open("temp.bat","w+") # Cerates the bat file that will be used to get the initial network information
	file.write("@echo off\nNETSH WLAN SHOW PROFILE >info.txt")
	#The text here will be broken down into two lines and basically it tells the console not to print the command on it then gets all of the saved networks and saves them to a new file called info
	file.close()
	os.startfile("temp.bat")
	time.sleep(.5) #The sleep gives the program a delay, so it doesn’t delete the bat file until it has finished executing its code
	os.remove("temp.bat")
	#This block of code writes DOS batch code into a bat file that will be executed to cerate a list off all saved networks. Then python deletes the bat file
	file=open("info.txt","r")
	info=file.read()
	# This open the file back up and makes it readable
	piecesOfInfo=info.splitlines() # This breaks the text from the info document into separate lines so the program can sort through it
	for i in range(len(piecesOfInfo)):
		temp=piecesOfInfo[i]
		if "All User Profile" in temp:
			temp=temp.split(":")
			networks.append(temp[1].strip())
# This block of code looks at each line to see if it contains the words “All User Profile”, if the program finds them 
# then the program ‘plucks” out the network names from the rest of the string and adds them to a list of networks names that will be used later on in the program	
	return networks

def getWiFiPassword(networkTarget,networkPassword):
	file=open("temp.bat","w+") # Cerates the bat file that will be used to get the Wi-Fi Password 
	text=["@echo off"]
	editMe="\nnetsh wlan show profile name=\""+networkTarget+"\" key=clear > temp1.txt"
	text.append(editMe)
	file.writelines(text)
	file.close()
	#This block of codes adds in the “network target” into a bat file so it can be run to find the Wi-Fi password. It uses the language DOS batch
	os.startfile("temp.bat") # This executes the DOS batch code
	time.sleep(.5) #The sleep gives the program a delay, so it doesn’t delete the bat file until it has finished executing its code
	os.remove("temp.bat")
	file=open("temp1.txt","r") # This open the file back up and makes it readable
	info=file.read() 
	piecesOfInfo=info.splitlines() # This breaks the text from the info document into separate lines so the program can sort through it
	for i in range(len(piecesOfInfo)):
		temp=piecesOfInfo[i]
		if "Key Content" in temp:
			temp=temp.split(":")
			networkPassword=temp[1].strip()
			# This block of code looks at each line to see if it contains the words “Key Content”, if the program finds them 
			# then the program ‘plucks” out the Wi-Fi password from the rest of the string and saves it
			return networkPassword

def exportData(dataToExport):
	file=open("Wi-Fi Password Finder.txt","w+") # Cerates the text file that will be used to store the Wi-Fi Password 
	file.writelines(dataToExport)
	file.close()
	# This bit writes the text to the file
	if os.path.isfile("temp1.txt"): os.remove("temp1.txt") # Because the method was recalled, the program will need to redelete the file if it still exists
	print("File successfully exported to the save location as where this program is running from")
	print("Press enter to continue")
	input()

cls()
print("Welcome to the Wi-Fi password finder program before the program runs there are a few things that you, the user, need to know. Since you we are able to get this program running, I assume that you have at least a basic understanding of computers and are able to understand the following:")
print("\nThe program may not run smoothly and may even crash if the account you’re on does not have admin or at least access to the cmd")
print("This program should run on the computer itself. Not a portable HDD, SSD or USB.")
print("Your computers antivirus may flag this program but and prevent you from running it")
print("I recommend that you maximise this program’s tab other wise the text may appear squished")
print("If you understand this and you are following the instruction type \"y\" and press enter to continue. Other wise just press enter and the program will exit")
x=input()
if x!="y": exit(0)
cls()
print("The goal of the project is to be able to list off all of the networks that your computer has saved and then extract their passwords. This is for educational proposes only and I am not responsible with what you do with it.")
print("If the flowing criteria is met, then type \"y\" and hit enter other wise just press enter and the program will close")
print("\nThe computer is currently connected to Wi-Fi (Not Ethernet)")
print("You have admin on the computer or least access to the cmd")
print("You are allowed to know your Wi-Fi credentials\n")
q=input()
if q!="y": exit(0)
cls()
print("This program may cerate pop up windows and temporary files, DO Not interact with them as the program will clean it all up then it is done")
print("This program will leave no trace but at the end the user will be given the option to export a log")
print("Press enter to start")
input()
cls()
# This bit of text is a warning and also makes sure that the user knows what they are doing

networks=[] # This cerates a list that will hold all of the network names
setUp(networks) #This runs the method that will set up the program by grabbing all of the network names
networkTarget="" # This will be used later to “target” or pick the network
time.sleep(.2) #The sleep gives the program a delay, so it doesn’t delete the bat file until it has finished executing its code
os.remove("info.txt") #By this time the program should be finished with the text file so it can be deleted 
networkPassword=""
dataToExport=[""]
while True: # This keeps the program looping so that the user enters a valid input but also makes it possible to return to this point
	cls()
	print("Welcome to the Wi-Fi password finder")
	print("Below is a list of all networks the program can access, type the number beside the name and press enter to get its password")
	print("type “all”, then press enter to display all of the available Wi-Fi passwords")
	print("Or type “e” to exit the program\n")
	for i in range(len(networks)):
		print(str(i+1)+")",networks[i])
	#This prints out all of the network names with a number beside them so that the user can make a choice
	u=input()
	if u=="e": exit(0)
	if u.isnumeric()==True:
		n=int(u) 
		if n>0 and n<=len(networks): # This bit checks if the input is a number then sees if it matches a network name
			cls()
			networkTarget= networks[n-1] # This bit converts the number over into the network name so that it can be used later on in the program
			print("Success:")
			print(networkTarget+":",getWiFiPassword(networkTarget,networkPassword)) # This calls on a method that will get the network passwords and returns them
			time.sleep(.2) # Gives the computer a little extra time to use the text file before deleting it just in case
			os.remove("temp1.txt") #By this time the program should be finished with the text file so it can be deleted 
			print("Press enter to be taken back to the Wi-Fi password finder screed or type e and press enter to exit")
			print("Or type “export” to export the data to text file on your desktop")
			c=input()
			if c=="e": exit(0)
			if c=="export":
			 dataToExport=networkTarget+":"+str(getWiFiPassword(networkTarget,networkPassword))
			 exportData(dataToExport) 
	if u=="all":
		cls()
		print("Success:")
		for i in range(len(networks)):
			networkTarget=networks[i]
			print(networkTarget+":",getWiFiPassword(networkTarget,networkPassword)) #This sets the target to the current network, gets its password and repeats
			dataToExport.append(networkTarget+":"+str(getWiFiPassword(networkTarget,networkPassword))+"\n")
		time.sleep(.2) # Gives the computer a little extra time to use the text file before deleting it just in case
		if os.path.isfile("temp1.txt"): os.remove("temp1.txt") #By this time the program should be finished with the text file so it can be deleted 
		print("Press enter to be taken back to the Wi-Fi password finder screed or type e and press enter to exit")
		print("Or type “export” to export the data to text file on your desktop")
		c=input()
		if c=="e": exit(0)
		if c=="export":
			 exportData(dataToExport)
