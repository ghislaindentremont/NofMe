# this script will for the appropriate inputs for workout b 

import os
import time 


# check that file exists, if so append to it, if not create it
if os.path.isfile("workout b"): 
	f = open("workout b", "a")
else:
	f = open("workout b", "w")
	header = [
	'Date'
	,'Chest_press_weight'
	,'Chest_press_rep'
	,'Leg_press_weight'
	]
	for item in header:
		f.write("%s\t" % item)
	# make this last
	f.write("%s" % 'Leg_press_rep')

# define all variables which will then be added on new line, mostly by prompting user 
date = time.strftime("%d/%m/%Y")
print "How much weight did you lift for your chest press?"
chest_press_weight = raw_input()
print "How many reps did you complete for your chest press?"
chest_press_rep = raw_input()
print "How much weight did you lift for your leg press?"
leg_press_weight = raw_input()
print "How many reps did you complete for your leg press?"
leg_press_rep = raw_input()	

# make list of variables
variables = [
	date
	,chest_press_weight
	,chest_press_rep
	,leg_press_weight	
	]

# write variables into file 
f.write("\n")
for item in variables:
	f.write(item+"\t")
# make this last
f.write(leg_press_rep)	

