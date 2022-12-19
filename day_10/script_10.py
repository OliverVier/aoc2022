cycles = {
    'noop':1,
    'addx':2
}

def task1(input):
    for i in range(0, len(input), 1):
        input[i] = input[i][:-1].split(" ")
    X = 1
    totalSignalStrength = 0

    totalCycleCount = 1 # start-value = 1

    for array in input:

        #While the cycle
        currentCycleCount = 0
        while(currentCycleCount < int(cycles.get(array[0]))):
            #Determine signal strength
            if((totalCycleCount % (40))-20 == 0):
                totalSignalStrength += totalCycleCount * X
            if(totalCycleCount == 240): # If the 240th cycle is reached, stop the program
                break

            currentCycleCount += 1
            totalCycleCount += 1

        if(totalCycleCount == 240): # If the 240th cycle is reached, stop the program
            break

        #After the cycle
        if(array[0] == "addx"):
            X += int(array[1])

    print("Solution 1: ", totalSignalStrength)

def task2(input):
    for i in range(0, len(input), 1):
        input[i] = input[i][:-1].split(" ")
    X = 1

    characters=[]
    stringList = []
    charIdx = 0

    for array in input:

        #While the cycle
        currentCycleCount = 0
        while(currentCycleCount < int(cycles.get(array[0]))):
            currentCycleCount += 1

            if((charIdx+1) >= X and (charIdx+1) <= X+2):
                characters.append("#")
            else:
                characters.append(" ") #Better readability without '.'
            charIdx+=1

            if((charIdx % 40) == 0):
                string = ""
                for char in characters:
                    string += char
                stringList.append(string)
                characters = []
                #Reset
                charIdx = 0

        #After the cycle
        if(array[0] == "addx"):
            X += int(array[1])
    
    print("Solution 2: ")
    for line in stringList:
        print(line)
        
with open("day_10/script_10_values.txt") as file:
    input = file.readlines()
    task1(input.copy())
    task2(input.copy())

        