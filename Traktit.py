# TrackedIt Main, version 0.0.1
# Copyright (c) by Tristan Miano Nov. 2013

import Activities #Like 94.88% of the program is in here
import pickle

try:
	filehandler = open('TrackedIt_Data.obj', 'r')
	ListOfUsers = pickle.load(filehandler)
except:
	ListOfUsers = Activities.UserList()
	print "\nNo Data found. Creating new file for data storage."

print "\nHello, and welcome to TrackedIt version 0.0.1"
print "\nCreated by Tristan Miano, Nov. 2013"

close = 0
while (close != 1):
	close = Activities.MenuMain(ListOfUsers)

filefordata = open('TrackedIt_Data.obj', 'w')
pickle.dump(ListOfUsers, filefordata)
