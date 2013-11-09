# Activities.py 
# Contains functions and classes related to the creation of a user and their activities.


#A user-defined variable to be included in the Activity class, only supports a name and a numerical value for the moment. Will improve!
class Detail:
	def __init__(self):
		self.name = ''
		self.somevalue = ''

	def setName(self):
		self.name = raw_input("\nWhat should we call this new variable? : ")
		print "\nCreated new detail: " + self.name
	
	def setValue(self):
		try:
			print "Enter the value for", self.name 
			self.somevalue = raw_input(": ")
		except:
			print "\nI don't think that's a valid input."
		
		print self.name + " = " + self.somevalue
	
	
#The generalized Activity class. This class will necessarily get larger and more complicated as we improve the program.
class Activity:
	def __init__(self):
		self.name = ''
		self.mood = []
		self.date = ''
		self.duration = []
		self.details = []

	def setName(self):
		self.name = raw_input("\nEnter the name of your new activity: ")

	def setName2(self, some_string):
		self.name = str(some_string)

	def getName(self):
		return self.name
	
	def setMood(self):
		try: 
			exit = 0
			while (exit != 1):
				self.mood = int(input("On a scale from 1 to 10, how happy were you during this activity? : "))
				if (self.mood < 1 or self.mood > 10):
					print "\nRemember, your rating must be a numerical value between 1 and 10."
				else:
					exit = 1

		except:
			print "\nSorry, that is not a valid inpust!"

	def getMood(self):
		return self.mood

	def setDate(self):
		try: 
			self.date = ''
			exit = 0
			while (exit != 1):
				month = int(input("\nDuring what month did you do this activity (MM): "))
				if (month < 1 or month > 12):
					print "\nHmm, I don't think that's a month."
				else:
					self.date = self.date + str(month)
					exit = 1
			exit = 0
			while (exit != 1):
				day = int(input("\nOn what day? (D): "))
				if (day > 31 or day < 1):
					print "\nHmm, I don't think that's a day."
				else:
					self.date = self.date + "/" + str(day)
					exit = 1
			exit = 0
			while (exit != 1):
				year = int(input("\nWhat year (YYYY): "))
				if year > 2013:
					print "\nI doubt that."
				else:
					self.date = self.date + "/" + str(year)
					exit = 1
			exit = 0
			while (exit != 1):
				try:
					hour = int(input("\nWhat hour during the day? (use '0' to '23' format): "))
					if (hour < 0 or hour > 23):
						print "\nUse '0' to '23' format, please."
					else:
						if len(str(hour)) < 2:
							hour = '0' + str(hour)

						self.date = self.date + " @ " + str(hour)
						exit = 1
				except:
					print "\nHmm, I didn't understand that input."
			exit = 0
			while (exit != 1):
				try:
					minutes = int(input("Minutes? (use '0' to '59' format): "))
					if (minutes < 0 or minutes > 59):
						print "\nUse '00' to '59' format, please."
					else:
						if len(str(minutes)) < 2:
							minutes = '0' + str(minutes)

						self.date = self.date + str(minutes)
						exit = 1
				except:
					print "\nHmm, I didn't understand that input."

		except:
			print "\nSorry, that is not a valid input!"

	def setDuration(self):
		try: 
			self.duration = input("In minutes, about how long did you spend doing this activity? :")

		except:
			print "\nSorry, that is not a valid input!"

	def getDuration(self):
		return self.duration
	
	def addDetail(self):
		detaillen = len(self.details)
		self.details.append(0)
		self.details[detaillen] = Detail()
		self.details[detaillen].setName()

	def passAttributes(self, ActivityInstance):
		self.name = ActivityInstance.name
		self.details = ActivityInstance.details

	def editDetail(self, index):
		self.details[index].setValue()

	def listActivityProperties(self):
		detaillen = len(self.details)
		print "\nActivity Name: " , self.name
		print "\nYour enjoyed it this much: ", self.mood
		print "\nYou enjoyed it on this date: ", self.date
		print "\nYou enjoyed it for this long: " + str(self.duration) + " minutes"
		for i in range(detaillen):
			print "\n" + self.details[i].name + ": " + self.details[i].somevalue


#But in case the user wants to create more than one instance of a certain activity, we also need a class which adds to a list of that same activity.
class ActivitySeries():
	def __init__(self):
		self.seriesname = ''
		self.SeriesList = []

	def setName(self):
		self.seriesname = raw_input("\nEnter the name of your new activity: ")

	def AddInstance(self):
		SeriesLen = len(self.SeriesList)
		self.SeriesList.append(0)
		self.SeriesList[SeriesLen] = Activity()
		self.SeriesList[SeriesLen].name = self.seriesname
		
	def listActivitySeriesProperties(self):
		SeriesLen = len(self.SeriesList)
		print "\nSeries Name: " + self.seriesname
		for i in range(SeriesLen):
			self.SeriesList[i].listActivityProperties()


	
# The User Class. Contains the user's name and list of activities, as well as a function to add a new activity. 
class User:
	def __init__(self):
		self.name = []
		self.ActivityList = []
		self.ActvSeriesList = []

	def CreateActivity(self):
		try: 
			yesno = raw_input("\nIs this something that you will be doing regularly? \n(default yes, otherwise type 'no'): ")
			if (yesno != 'no'):
				seriesLen = len(self.ActvSeriesList)
				self.ActvSeriesList.append(0)
				self.ActvSeriesList[seriesLen] = ActivitySeries()
				self.ActvSeriesList[seriesLen].setName()
				print "\nCreated activity: " + self.ActvSeriesList[seriesLen].seriesname
			else:
				activlen = len(self.ActivityList)
				self.ActivityList.append(0)
				self.ActivityList[activlen] = Activity()
				self.ActivityList[activlen].setName()
				print "\nCreated one-time activity: " + self.ActivityList[activlen].name
		except:
			print "\nInvalid Input."
	
	def AddToSeries(self, index):
		self.ActvSeriesList[index].AddInstance()
	
	def ViewActivities(self):
		if len(self.ActvSeriesList) > 0:
			print "\nHere are your regular activities: "
			for i in range(len(self.ActvSeriesList)):
				print "\n" + str(i+1) + ". " + self.ActvSeriesList[i].seriesname
		else:
			print "\nYou have no regular activities yet."
		if len(self.ActivityList) > 0:
			print "\nHere is your list of one-time activities: "
			for i in range(len(self.ActivityList)):
				print "\n" + str(i+len(self.ActvSeriesList)+1) + ". " + self.ActivityList[i].name
		else:
			print "\nYou haven't created any one-time activities yet."

	def setName(self, username):
		self.name = username
	
#But we also need a class which contains each of the User Objects, and can be added to. 
class UserList:
	def __init__(self):
		self.ListofUsers = []

	def AddUser(self, username):
		UserListLen = len(self.ListofUsers)
		self.ListofUsers.append(0)
		self.ListofUsers[UserListLen] = User()
		self.ListofUsers[UserListLen].setName(username)


# FUNCTIONS
		
#Function to add new user to profile list		
def CreateProfile(UserList):
	try:
		userx = raw_input("\nState the name of the new user: ")
		print "\nExcellent. Hello " + userx + ". Welcome to Trak't It!"
		UserList.AddUser(userx)
	except: 
		print "\nError: Are you sure that's your real name?"
	


# The Main Menu
def MenuMain(UserList):
	exit = 0
	
	while (exit != 1):
		print "\n *****MAIN MENU*****"
		print "\n1. Create Profile \n2. Select Profile \n3. Exit Program \n"

		try: 
			choice = input("\nMake your selection: ")
			if choice == 1:
				CreateProfile(UserList)
			elif choice == 2:
				ProfileMenu(UserList)
			elif choice == 3:
				exit = 1
			else:
				print "\nInvalid Menu Selection.\n"
		except:
			print "\nThat is not a valid entry."

	return 1

# Selecting a Profile
def ProfileMenu(UserList):
	exit = 0
	ProfileLength = len(UserList.ListofUsers) 

	while (exit != 1):
		for i in range(ProfileLength):
			print  str(i+1) + ". " + UserList.ListofUsers[i].name

		print "\n" + str(ProfileLength+1) + ". Exit"
		try:
			choice = input("\nMake your selection: ") - 1
			if choice in range(ProfileLength):
				UserMenu(UserList.ListofUsers[choice])
			elif choice == ProfileLength:
				exit = 1
			else:
				print "\nSelection Not Available"
		except:
			print "\nI don't understand that input."
		


# The Activity Menu, where the user can choose to edit the details of an activity
def ActivMenu(Activity):
	exit = 0
	
	print "\nHere you may edit the details of an activity, such as mood, date, duration, or a detail of your choosing. "
		
	while (exit != 1):
		try:
			print "\n1. Set Mood \n2. Set Date \n3. Set Duration "
			detaillen = len(Activity.details)
			for i in range(detaillen):
				print str(i + 4) + ". Set " + Activity.details[i].name
	
			print "\n" + str(detaillen + 4 ) + ". Add New Detail" 
			print "\n" + str(detaillen + 5 ) + ". Exit"
			choice = input("\nMake your selection: ")
			
			if choice == 1:
				Activity.setMood()
			elif choice == 2:
				Activity.setDate()
			elif choice == 3:
				Activity.setDuration()
			elif choice - 4 in range(detaillen):
				Activity.editDetail(choice - 4)
			elif choice == detaillen + 4:
				Activity.addDetail()
			elif choice == detaillen + 5:
				exit = 1
			else:
				print "\nInvalid Selection."
		
			
		except:
			print "\nI don't understand that input."
	

# The Activity List, which allows the user to select an activity from a list of their regular and special activities.
def ActivListMenu(User):
	exit = 0
	
	while (exit != 1):
		try:
			print "\nPlease select one of your regular or one-time activities: "
			User.ViewActivities()
			SeriesListLen = len(User.ActvSeriesList)
			ActivLen = len(User.ActivityList)
			print "\n" + str(SeriesListLen + ActivLen + 1) + ". Exit"
			choice = input("\nMake your selection: ") - 1
	
			if choice in range(SeriesListLen):
				SeriesLen = len(User.ActvSeriesList[choice].SeriesList)
				print "\nPick an existing instance of this series or add a new instance. "
				if SeriesLen > 0:
					print "\nInstances of " + User.ActvSeriesList[choice].seriesname + ":"
					for i in range(SeriesLen):
						print "\n" + str(i+1) + ". " + User.ActvSeriesList[choice].SeriesList[i].date

				print "\n" + str(SeriesLen + 1) + ". Add New Instance "
				try:
					choice2 = input("\nMake your selection: ") - 1
			
					if choice2 in range(SeriesLen):
						User.ActvSeriesList[choice].SeriesList[choice2].listActivityProperties()
						ActivMenu(User.ActvSeriesList[choice].SeriesList[choice2])
					elif choice2 == SeriesLen:
						User.AddToSeries(choice)
						User.ActvSeriesList[choice].SeriesList[choice2].setDate()
					else:
						print "\nNot a valid selection. "
				except:
					print "\nI don't understand that input. "

			elif choice in range(ActivLen + SeriesListLen):
				User.ActivityList[choice - SeriesListLen].listActivityProperties()
				ActivMenu(User.ActivityList[choice - SeriesListLen])
			elif choice == SeriesListLen + ActivLen:
				exit = 1
			else: 
				print "\nThat is not a valid selection."
		
		except:
			print "\nThat is not a valid entry."
			

	
# The Main Menu for the User, can choose to create a new activity, or to view entire log.
def UserMenu(User):
	exit = 0
	print "\nWelcome Back, " + User.name + ". Here are your available options: "
	
	while (exit != 1):
		try:
			print "\n1. Create New Activity \n2. Select Activity \n3. View Personal Log \n4. Exit"
			choice = input("\nMake your selection: ")
			if choice == 1:
				User.CreateActivity()
			elif choice == 2:
				ActivListMenu(User)
			elif choice == 3:
				print "\nEverything you've ever done: "
				print "**************************************************"
				print "**************************************************"
				print "\nHere are your regular activities:"
				print "**************************************************"
				for i in range(len(User.ActvSeriesList)):
					User.ActvSeriesList[i].listActivitySeriesProperties()
				print "**************************************************"
				print "\nAnd here are your one-time activities:"
				for i in range(len(User.ActivityList)):
					User.ActivityList[i].listActivityProperties()

			elif choice == 4:
				exit = 1
			else:
				print "\nInvalid Menu Selection.\n"
			
		except:
			print "\nOops, that's not a proper input."
	
