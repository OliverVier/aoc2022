
def moveCrates(amount: int, from_pos: int, to_pos: int):
    from_pos -= 1
    to_pos -= 1

    data_copy = data_columns[from_pos][0:amount]
    
    data_copy.reverse() #Solution 2) Remove or comment out this line
    
    for command in data_copy:
        data_columns[from_pos].remove(command)
    
    data_columns[to_pos] = data_copy + data_columns[to_pos]

data = []
data_columns = []
commands = []

#Set this value manually!
column_size = 9

with open("day_5\script_5_values.txt") as file:
    lineList = []
    for line in file:
        lineList.append(line)

    data = lineList[0:column_size]
    commands = lineList[10:len(lineList)]

    for i in range(0,column_size,1):
        data_columns.append([])

    for row in range(0, len(data), 1):
        for col in range(0, column_size, 1):
            start = 4 * col
            if(data[row][start:start+4].strip() != ""):
                data_columns[col].append(data[row][start:start+4].strip())
    
    for commandIdx in range(0,len(commands), 1):
        commands[commandIdx] = commands[commandIdx].rstrip().split(" ")[1:6:2] #Move-, from- and to-values only

    for command in commands:
        moveCrates(int(command[0]),int(command[1]),int(command[2]))
   
    first_letters = ""
    for list in data_columns:
        first_letters += list[0]
    print("Solution: ", first_letters)