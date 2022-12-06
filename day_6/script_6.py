def findStartMarker(line):
    start_characters = [] #Always contains for characters
    sop_marker = 0
    is_Found = True 
    line_string = list(line)
    
    for i in range(0, len(line_string), 1):
        start_characters.append(line_string[i])
        if(len(start_characters) > 4):
            start_characters.remove(start_characters[0])
        if(len(start_characters) == 4):
            #Check characters, if they are all different
            for z in range(0, len(start_characters), 1):
                for k in range(0, len(start_characters), 1):
                    if(int(k) == int(z)):
                        continue
                    if(str(start_characters[z]) == str(start_characters[k])):
                        is_Found = False
            if(is_Found == True):
                sop_marker=i+1
                return start_characters, sop_marker      
            is_Found = True  

def findMessageMarker(line, startMarker):
    start_characters = [] #Always contains for characters
    sop_marker = 0
    is_Found = True 
    line_string = list(line)
    
    for i in range(startMarker-1, len(line_string), 1):
        start_characters.append(line_string[i])
        if(len(start_characters) > 14):
            start_characters.remove(start_characters[0])
        if(len(start_characters) == 14):
            #Check characters, if they are all different
            for z in range(0, len(start_characters), 1):
                for k in range(0, len(start_characters), 1):
                    if(int(k) == int(z)):
                        continue
                    if(str(start_characters[z]) == str(start_characters[k])):
                        is_Found = False
            if(is_Found == True):
                sop_marker=i+1
                return start_characters, sop_marker      
            is_Found = True   
          
with open("day_6\script_6_values.txt") as file:
    for line in file:
        marker = findStartMarker(line)
        print(findMessageMarker(line, 0))