# this is a script that will prompt me for biometrics input at the end of the day

import os.path
import time
import sys

# this takes my multi-line string and gets rid of all the spaces etc.
def trim(docstring):
    if not docstring:
        return ''
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxint
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxint:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\t'.join(trimmed)

# check that file exists, then change header
# this allows for adding new columns 
# ensure that you add corresponding variables
# DONT REMOVE HEADERS OR VARIABLES 
with open("data", 'r') as file: 
	data = file.readlines()
	header = """
	Date
	Fat
	Carb
	Protein	
	Fiber
	Calories
	Water						
	Poop_score_avg
	Poop_num
	Sleep_length
	Sleep_deep_prop
	Caffeine
	Mood
	Steps
	HRV
	Nicotine
	Alcohol
	Meditate
	"""
	data[0] = trim(header) 

	file.close()

with open("data", 'w') as file:
	file.writelines( data ) 

	file.close()


# define all variables which will then be added on new line, mostly by prompting user 		
print "Is this data for today? (True or False)",
date_bool = raw_input(">") 

if date_bool == "True": 
	date = time.strftime("%d/%m/%Y")
else:
	print "Ok, then what is the date of the data? (dd/mm/yyyy)",
	date = raw_input(">")
	
print "What percentage of your total calorie intake was fat today?",
fat = raw_input(">") 
print "What percentage of your total calorie intake was carb today?",
carb = raw_input(">")
print "What percentage of your total calorie intake was protein today?",
protein = raw_input(">")
print "How many grams of fiber did you consume today?",
fiber = raw_input(">")
print "How many calories did you consume today?",
calories = raw_input(">")
print "How many ounces of water did you consume today?",
water = raw_input(">")
print "What is the average kind of poop you had today?",
poop_score_avg = raw_input(">")						
print "How many poops did you take today?",
poop_num = raw_input(">")
print "How many hours did you sleep for last night?",
sleep_length = raw_input(">")
print "What percentage of your overall sleep was deep sleep last night?",
sleep_deep_prop = raw_input(">")
print "How many milligrams of caffeine did you consume today?",
caffeine = raw_input(">")
print "On a scale of 1 to 10, how was your mood today?",
mood = raw_input(">")
print "How many steps did you take today?",
steps = raw_input(">")
print "What was your average coherence today?",
hrv = raw_input(">")
print "How many times did you vapurize today?",
nicotine = raw_input(">")
print "How many drinks did you consume today?",
alcohol = raw_input(">")

# make this last
print "How long did you meditate for today (in mins.)? ",
meditate = raw_input(">") 

# make list of variables
variables = [
	date
	,fat
	,carb
	,protein	
	,fiber
	,calories
	,water							
	,poop_score_avg
	,poop_num
	,sleep_length
	,sleep_deep_prop
	,caffeine
	,mood
	,steps
	,hrv
	,nicotine
	,alcohol
	]


f = open("data", "a")
# write variables into file 
f.write("\n")
for item in variables:
	f.write(item)
	f.write("\t")
# make this last
f.write(meditate)
 
f.close()
