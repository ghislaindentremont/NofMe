# this is a script that will prompt me for biometrics input at the end of the day

import os.path
import time
import sys
from sys import argv 

# take data_type argument via powershell
script, data_type = argv

# create list of plausible arguments 
data_types = ["daily", "workoutA", "workoutB"]

# as long as argument given is not in list, keep asking for new argument
while data_type not in data_types:
	print "You have not specified an existing data file."
	print "Please choose from the following: %s, %s, %s" % (data_types[0], data_types[1], data_types[2])
	data_type = raw_input(">>>")

# get index of argument - this is the IMPORTANT variable and it is therefore important to maintain the same order of 'data types' between 'headers' and 'variables'
data_type_index = data_types.index(data_type)

# headers
header_daily = """
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

header_workoutA = """
Date
Pull_down_weight
Pull_down_rep
Shoulder_press_weight
Shoulder_press_rep
Bicep_curl_weight
Bicep_curl_rep
"""

header_workoutB = """
Date
Chest_press_weight
Chest_press_rep
Leg_press_weight
Leg_press_rep
Tricep_extention_weight
Tricep_extention_rep
"""

headers = []
headers.append(header_daily)
headers.append(header_workoutA)
headers.append(header_workoutB)


# variables/prompts 
question_daily = [
"What percentage of your total calorie intake was fat?"
,"What percentage of your total calorie intake was carb?"
,"What percentage of your total calorie intake was protein?"
,"How many grams of fiber did you consume?"
,"How many calories did you consume?"
,"How many ounces of water did you consume?"
,"What is the average kind of poop you had?"						
,"How many poops did you take?"
,"How many hours did you sleep for last night?"
,"What percentage of your overall sleep was deep sleep last night?"
,"How many milligrams of caffeine did you consume?"
,"On a scale of 1 to 10, how was your mood?"
,"How many steps did you take?"
,"What was your coherence score?"
,"How many times did you vapurize?"
,"How many drinks did you consume?"
,"How long did you meditate for today (in mins.)?" 
]

question_workoutA = [
"How much weight did you lift for your pull down?"
,"How many reps did you complete for your pull down?"
,"How much weight did you lift for your shoulder press?"
,"How many reps did you complete for your shoulder press?"	
,"How much weight did you lift for your bicep curl?"
,"How many reps did you complete for your bicep curl?"
]

question_workoutB = [
"How much weight did you lift for your chest press?"
,"How many reps did you complete for your chest press?"
,"How much weight did you lift for your leg press?"
,"How many reps did you complete for your leg press?"	
,"How much weight did you lift for your tricep extention?"
,"How many reps did you complete for your tricep extention?"	
]

questions = []
questions.append(question_daily)
questions.append(question_workoutA)
questions.append(question_workoutB)


# define some functions

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

# this asks user to specify the date if it is not today's, otherwise it does so automatically 
def what_date():
	global date

	date_bool = "hey" 
	bools = ["True", "False"]
	
	while date_bool not in  bools: 
		print "Is this data for today? (True or False)",
		date_bool = raw_input(">>>") 

		if date_bool == "True": 
			date = time.strftime("%d/%m/%Y")
		elif date_bool == "False":
			print "Ok, then what is the date of the data? (dd/mm/yyyy)",
			date = raw_input(">>>")

# cycle through questions and get answers, storing them in list 
# if BACK is entered for question n, ask question n - 1 again 
def get_answers():
	global answers 
	answers = []
	
#	for question in questions[data_type_index]:
#		if "BACK" not in answers:
#			temp = raw_input(">>> %s" % question)
#			index = questions[data_type_index].index(question)
#			answers[index] = temp
#		else:
#			index = questions[data_type_index].index(question) - 1
#			last_question = questions[data_type_index][index]
#			temp = raw_input(">>> %s" % last_question)

	for index in range(len(questions[data_type_index])):
		if index > 0:
			if answers[index - 1] == "BACK":
				question = questions[data_type_index][index - 2]
				temp = raw_input(">>> %s" % question)	
				answers[-2] = temp

				question = questions[data_type_index][index - 1]
				temp = raw_input(">>> %s" % question)	
				answers[-1] = temp

		question = questions[data_type_index][index]
		temp = raw_input(">>> %s" % question)
		answers.append(temp)
	
	if answers[-1] == "BACK":
		question = questions[data_type_index][-2]
		temp = raw_input(">>> %s" % question)	
		answers[-2] = temp

		question = questions[data_type_index][-1]
		temp = raw_input(">>> %s" % question)	
		answers[-1] = temp	

	happy = "hey"
	bools = ["True", "False"]

	while happy not in bools: 
		happy = raw_input(">>> Was your last entry proper? (True or False)")
		if happy == "True":
			pass
		elif happy == "False":
			question = questions[data_type_index][-1]
			temp = raw_input(">>> %s" % question)	
			answers[-1] = temp

# change header if needed, prompt user, append to file 
def prompt(data_type_index):
 	with open(data_types[data_type_index], 'r') as file:
		data = file.readlines()

		header = headers[data_type_index]

		data[0] = trim(header) + "\n"

		file.close()

	with open(data_types[data_type_index], 'w') as file:
		file.writelines( data ) 

		file.close()

	what_date()

	get_answers()

	f = open(data_types[data_type_index], "a")
	
	# write variables into file 
	f.write("\n")
	f.write(date)
	f.write("\t")
	for item in answers[:-1]:
		f.write(item)
		f.write("\t")
	
	# make this last
	f.write(answers[-1])
	 
	f.close()



# prompt user for relevant inputs
prompt(data_type_index)
























