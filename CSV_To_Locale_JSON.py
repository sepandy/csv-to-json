import csv
import json 

# ask for file path in console
file_path = input("Enter file path: ")

# open file
with open(file_path, 'r') as csv_file:
	# read file
	csv_reader = csv.reader(csv_file, delimiter=",", quotechar='"')
	
	data = []
	
	for row in csv_reader:
		
		data.append(row)

# pop first row from list
languages = data.pop(0)
# print(data)
# create empty dictionary
# make an array of dictionaries per language
locales = []
for language in languages:
	locales.append({})

for row in data:
	# loop from second item in row to last item in row
	key = row[0]
	for i in range(len(row)):
		# if value is not empty
		if row[i] != '':
			# add key and value to dictionary
			locales[i][key] = row[i]

# write result in files
for i in range(len(locales)):
	with open(languages[i] + '.json', 'w') as json_file:
		json_object = json.dumps(locales[i], indent = 4) 
		json_file.write(json_object)
		json_file.close()
		print("File " + languages[i] + '.json' + " created.")
