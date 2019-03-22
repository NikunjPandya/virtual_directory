"""
AUTHOR - NIKUNJ PANDYA
EMAIL  - nikunjpandya@outlook.com
PHONE  - 8320190985
"""

class Directory():
	'''
	DIRECTORY CLASS TO HOLD PATH AND SUBPATH INFORMATION
	'''

	# default constructor method
	def __init__(self, name=None, parent=None):
		self.parent = parent
		self.name = name
		self.sub_dir=[]

	# Add Directory
	def add_dir(self, dir_name):
		directory = Directory(name=dir_name, parent=self)
		self.sub_dir.append(directory)

	# Check if Directory exists
	def is_dir(self, dir_name):
		for directory in self.sub_dir:
			if directory.name == dir_name:
				return True
		return False

	# Remove directory if found
	def delete_dir(self, dir_name):
		for i, directory in enumerate(self.sub_dir):
			if directory.name == dir_name:
				self.sub_dir.pop(i)
				break
				return True
		return False

	# Return requested subdirectory
	def return_directory(self, dir_name):
		for directory in self.sub_dir:
			if directory.name == dir_name:
				return directory
		return None

	# Return parent directory path recursively
	def return_parent_path(self):
		if self.parent == None or self.name==None:
			return ""
		return self.parent.return_parent_path()+self.name+'/'

# control variable for function
exit = False

print "Application started...\n"

# INIT
root = Directory()
# Current directory tracker object
current_dir = root
while(not exit):
	# Input variables
	input = raw_input("$ ")
	input_arr = input.split(" ")

	# Flag to escape loop errors
	invalid = False

	# Switch case style actions on primary command
	if not input:
		print "ERR: COMMAND MISSING"

	# Session Clear
	elif input == "session clear":
		print "SUCC: CLEARED: RESET TO ROOT"
		current_dir = Directory()

	# Exit program
	elif input == "exit":
		exit = True

	# Iterate subdirectories and print names
	elif input_arr[0] == 'ls':
		print("DIRS: "),
		for sub_dir in current_dir.sub_dir:
			print(sub_dir.name),
		print ""

	# Print current directory location
	elif input_arr[0] == 'pwd':
		print "PATH: /"+ current_dir.return_parent_path()[:-1]

	# Create Directory
	elif input_arr[0] == 'mkdir':
		# Check if path given
		if len(input_arr) == 1:
			print "ERR: PATH MISSING"
			continue
		# Split given path
		paths = input_arr[1].split("/")
		# Check if operation on root directory or current
		if input_arr[1][0] == '/':
			working_dir = root
		else:
			working_dir = current_dir
		# Iterate till second last sub-path and create final directory
		for i in range(0, len(paths)-1):
			if not paths[i]:
				continue
			if not working_dir.is_dir(paths[i]):
				print "ERR: PATH INVALID"
				invalid = True
				break
			working_dir = working_dir.return_directory(paths[i])
		if invalid:
			continue
		if working_dir.is_dir(paths[len(paths)-1]):
			print "ERR: DIRECTORY ALREADY EXISTS"
		else:
			working_dir.add_dir(paths[len(paths)-1])
			print "SUCC: CREATED"

	# Change current Directory
	elif input_arr[0] == 'cd':
		# Check if path given
		if len(input_arr) == 1:
			print "ERR: PATH MISSING"
			continue
		# Case to move up a Directory
		if input_arr[1] == '..':
			if not current_dir.parent:
				print "ERR: ALREADY AT ROOT DIRECTORY"
				continue
			current_dir = current_dir.parent
			print "SUCC: REACHED"
			continue
		# Split given path
		paths = input_arr[1].split("/")
		# Check if operation on root directory or current
		if input_arr[1][0] == '/':
			working_dir = root
		else:
			working_dir = current_dir
		# Iterate all subpaths to reach final directory
		for i in paths:
			if not i:
				continue
			if not working_dir.is_dir(i):
				print "ERR: INVALID PATH"
				invalid = True
				break
			working_dir = working_dir.return_directory(i)
		if invalid:
			continue
		current_dir = working_dir
		print "SUCC: REACHED"

	# Remove Directory
	elif input_arr[0] == 'rm':
		# Check if path given
		if len(input_arr) == 1:
			print "ERR: PATH MISSING"
			continue
		# Split given path
		paths = input_arr[1].split("/")
		# Check if operation on root directory or current
		if input_arr[1][0] == '/':
			working_dir = root
		else:
			working_dir = current_dir
		# Iterate till second last sub-path and remove final directory
		for i in range(0, len(paths)-1):
			if not paths[i]:
				continue
			if not working_dir.is_dir(paths[i]):
				print "ERR: PATH INVALID"
				invalid = True
				break
			working_dir = working_dir.return_directory(paths[i])
		if invalid:
			continue
		if working_dir.is_dir(paths[len(paths)-1]):
			working_dir.delete_dir(paths[len(paths)-1])
			print "SUCC: DELETED"
		else:
			print "ERR: DIRECTORY DOESN'T EXISTS"
	else:
		print "ERR: CANNOT RECOGNIZE INPUT"
	# exit = False