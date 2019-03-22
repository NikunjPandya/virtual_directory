# Virtual Directory
A linux virtual Directory in python

@@@
Author - Nikunj Pandya
Email  - nikunjpandya@outlook.com
@@@

Please note the program is coded in Python 2.7 and following is the technical description of commands and how to run.

The program simulates a file directory system.

To run, open the current directory (containing script.py) in terminal and run following command:

```python scripy.py```

Following are the list of supported commands: 

1. ls

Take no argument and shows current directory

OUTPUT FORMAT:

	DIRS: home Desktop

2. pwd

Takes no argument and shows current path with respect to root directory.

OUTPUT FORMAT: 

	PATH: /home

3. exit

Takes no argument and exists the program safely.

4. session clear

Clears the current session and restarts program from scratch.

OUTPUT FORMAT: 
	
	"SUCC: CLEARED: RESET TO ROOT"

4. cd <path>

Changes the current location.

	i. path == "..":
		Takes to parent directory when given command "cd .." and returns error message if already at root directory.

	ii. path == "/":
		Takes to root directory.

	iii. path starts with "/":
		Assumes path w.r.t to root directory.

	iv. path like home/Desktop:
		Assumes current directory.

OUTPUT FORMAT:
	
	"ERR: PATH MISSING" -> No Path given

	"ERR: ALREADY AT ROOT DIRECTORY" -> When moving up directory but already at root.

	"ERR: INVALID PATH" -> Invalid Path which doesn't exists.

	"SUCC: REACHED" -> Moving to valid path.

5. mkdir <path>

Creates directory at specified path location.

	i. path starts with "/":
		Assumes w.r.t to root directory.

	ii. path like home/Desktop:
		Assumes current directory.

OUTPUT FORMAT:

	"ERR: PATH MISSING" -> No path given.

	"ERR: PATH INVALID" -> Invalid path which doesn't exists.

	"ERR: DIRECTORY ALREADY EXISTS" -> Directory with given name already exists at path.

	"SUCC: CREATED" -> Directory created.

6. rm <path>

Deletes directory at specified path location.

	i. path starts with "/":
		Assumes w.r.t to root directory.

	ii. path like home/Desktop:
		Assumes current directory.

OUTPUT FORMAT:

	"ERR: PATH MISSING" -> No path given.

	"ERR: PATH INVALID" -> Invalid path which doesn't exists.

	"ERR: DIRECTORY DOESN'T EXISTS" -> Directory to delete does not exists at path.

	"SUCC: DELETED" -> Directory deleted.

7. Any other input:

OUTPUT FORMAT:
	
	"ERR: CANNOT RECOGNIZE INPUT"
