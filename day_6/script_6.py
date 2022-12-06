#View the commit-history to see my first solution of day 6

def findMarker(line, searchSize, startIdx=0):
    start_characters = [] #Always contains for characters
    is_Found = True 
    line_string = list(line)

    if(startIdx < 0):
        startIdx = 0
    
    for i in range(startIdx, len(line_string), 1):
        start_characters.append(line_string[i])
        if(len(start_characters) > searchSize):
            start_characters.remove(start_characters[0])
        if(len(start_characters) == searchSize):
            for z in range(0, len(start_characters), 1):
                for k in range(0, len(start_characters), 1):
                    if(int(k) == int(z)):
                        continue
                    if(str(start_characters[z]) == str(start_characters[k])):
                        is_Found = False
            if(is_Found == True):
                return start_characters, i   
            is_Found = True   
          
with open("day_6\script_6_values.txt") as file:
    for line in file:
        startMarker = findMarker(line=line, searchSize=4, startIdx=0)
        messageMarker = findMarker(line=line, searchSize=14, startIdx=int(startMarker[1]))
        print(f"Solution 1) Start-of-packet after {int(startMarker[1])+1} characters")
        print(f"Solution 2) Start-of-message after {int(messageMarker[1])+1} characters")