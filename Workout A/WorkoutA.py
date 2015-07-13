# this script will ask for the appropriate inputs for workout a

import os
import time 


# check that file exists, if so append to it, if not create it
if os.path.isfile("workout a"): 
	f = open("workout a", "a")
else:
	f = open("workout a", "w")
	header = [
	'Date'
	,'Pull_down_weight'
	,'Pull_down_rep'
	,'Shoulder_press_weight'
	]
	for item in header:
		f.write("%s\t" % item)
	# make this last
	f.write("%s" % 'Shoulder_press_rep')

# define all variables which will then be added on new line, mostly by prompting user 
date = time.strftime("%d/%m/%Y")
print "How much weight did you lift for your pull down?"
pull_down_weight = raw_input()
print "How many reps did you complete for your pull down?"
pull_down_rep = raw_input()
print "How much weight did you lift for your shoulder press?"
shoulder_press_weight = raw_input()
print "How many reps did you complete for your shoulder press?"
shoulder_press_rep = raw_input()	

# make list of variables
variables = [
	date
	,pull_down_weight
	,pull_down_rep
	,shoulder_press_weight	
	]

# write variables into file 
f.write("\n")
for item in variables:
	f.write(item+"\t")
# make this last
f.write(shoulder_press_rep)

