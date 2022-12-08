line_string = []
directories = {}

def readInput():
	with open("day_7\script_7_values.txt") as file:
		for line in file:
			line_string.append(line.split(" "))
			lastElementIdx = len(line_string)-1
			lastItemIdx = len(line_string[lastElementIdx])-1
			line_string[lastElementIdx][lastItemIdx] = line_string[lastElementIdx][lastItemIdx][:-1] #Remove "\n"
				

def createDirectories():
	global line_string
	global directories

	directories['Oliver'] = {'size': 0} #Starting point
	
	current_dict = directories.get('Oliver')
	recent_dict_list = []

	for command in line_string:

		if(len(command) == 3):                          # USING CD
			
			if(command[2] == ".."):                     # GO BACK ONCE
				item = recent_dict_list.pop()
				current_dict = item
				
			elif(current_dict.get(command[2]) == None): # DIRECTORY UNKNOWN - CREATE
				recent_dict_list.append(current_dict)
				current_dict[command[2]] = {'size': 0}
				current_dict = current_dict.get(command[2])        

			else:                                       # DIRECTORY KNOWN
				recent_dict_list.append(current_dict)
				current_dict = current_dict.get(command[2])

		else:                                           # LS - LIST DIRECTORIES AND FILES
			if(command[0] != "$" and command[0] != "dir"):
				current_dict[command[1]] = command[0]
				
def calculateDirectorySpace(directory: dict):
	global line_string
	items = list(directory)
	totalSum = 0

	for item in items:
		if(type(directory.get(item)) == str): #Ignore the 'int'-item => 'size'
			totalSum += int(directory.get(item))
		if(type(directory.get(item)) == dict):
			totalSum += calculateDirectorySpace(directory[item])
	
	directory['size'] = int(totalSum)
	
	return totalSum

def calculateSumOfSpace(directory: dict, sizeSmallerThan: int) -> int:
	global line_string

	items = list(directory)
	totalSum = 0    

	for item in items:
		if(type(directory.get(item)) == int and directory.get(item) <= sizeSmallerThan):
			totalSum += int(directory.get(item))
		elif(type(directory.get(item)) == dict):
			totalSum += calculateSumOfSpace(directory[item], sizeSmallerThan=100000)
		
	return totalSum

def getDirectorySizeList(directory: dict) -> list:
	global line_string

	items = list(directory)
	sumList = []
		
	for item in items:
		if(type(directory.get(item)) == int):
			sumList.append(directory.get(item))
		elif(type(directory.get(item)) == dict):
			sumList = sumList + (getDirectorySizeList(directory[item]))
		
	return sumList

readInput()
createDirectories()

calculateDirectorySpace(directories["Oliver"])
print("Task 1) Sum of directories (of files which are smaller than 100.000): ", calculateSumOfSpace(directory=directories["Oliver"], sizeSmallerThan=100000))

directorySizeList = getDirectorySizeList(directory=directories["Oliver"]["/"])
directorySizeList.sort()

totalSpace = 70000000
requiredSpace = 30000000
unusedSpace = totalSpace - directorySizeList[-1]

smallestValue = 0
for item in directorySizeList:
	if(item+unusedSpace > requiredSpace):
		print(f"Task 2) Delete the directory with a size of {item}")
		break

