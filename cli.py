import pandas
import os
import sys
import re

# Read the command line arguments and check wether they are valid
def command_reader():
	if len(sys.argv) < 3:
		print("You provided too little arguments")
	elif len(sys.argv) > 3:
		print("You provided too many arguments")
	elif sys.argv[1] == "--name":
		return sys.argv[2]
	return

# Function that reads the input from a CSV file that is located at a github repository, pointed to by a URL
# After reading the input, the function converts the data to a usable format
def read_input():
	source_data_url = "https://raw.githubusercontent.com/infi-nl/everybody-codes/master/data/cameras-defb.csv"

	data_frame = pandas.read_csv(source_data_url)

	numpy_data = data_frame.to_numpy()

	list_data = numpy_data.tolist()

	return list_data

# Loop through the data and return a list of all the rows where an occurence
# of the '--name' is found.
def find_matching_rows(name):
	data = read_input()

	found_occurences = []
	for line in data:
		if line[0].count(name) > 0:
			found_occurences.append(line[0])
	return found_occurences

# Format the rows from the dataset into the correct form.
def format_rows(data):
	formatted_rows = []
	for string in data:
		string = re.split(r';', string)
		prefix_string = re.split(r'-| ', string[0])
		new_string = prefix_string[2] + ' | '  + string[0] + ' | ' + string[1] + ' | ' + string[2]
		formatted_rows.append(new_string)
	return formatted_rows

# Check if the arguments passed to cli.py are valid, and call the functions that
# return the matching rows in the data. After that the returned rows are formatted
# and printed for the user to see.
def main():
	searched_name = command_reader()
	if len(searched_name) == 0:
		print("That option is invalid")
	else:
		matching_rows = find_matching_rows(searched_name)
		formatted_rows = format_rows(matching_rows)
		for entry in formatted_rows:
			print(entry)

if __name__ == '__main__':
	main()