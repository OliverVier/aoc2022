import re

#Used for item-priority
#a-z 1-26 && A-Z 27-52
#One space at the beginning => index of a starts at 1, instead of 0
priorityString = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Split string into two halfs
def splitString(string:str):
    line_string = list(line)
    #Last entry always contains \n, so we want the second substr to be at len(string)-1
    return [list(line_string[0:int((len(string)/2))]),
            list(line_string[int((len(string)/2)):len(string)-1])]


### Task 1

sumKeyPriority = 0
key_map = {}
compartments = []

with open("day_3\script_3_values.txt") as file:
    for line in file:
        compartments = splitString(line)        
        for key in compartments[0]:
            key_amount_L1 = compartments[0].count(key)
            key_amount_L2 = compartments[1].count(key)
            if(key_amount_L1 > 0 and key_amount_L2 > 0):
                key_map[key] = ""
        for map_key in key_map:
            sumKeyPriority += priorityString.find(map_key)
        key_map.clear()

print("Solution 1)", sumKeyPriority)

### Task 2

def findBadge(groupList: list) -> str:
    #Find the smallest backpack and use it as a reference
    smallestBackpack = min(groupList, key=len)
    groupList.remove(smallestBackpack)

    for key in smallestBackpack:
        if(containsItem(groupList[0], key) and containsItem(groupList[1], key)):
            return key
    return None
            
def containsItem(group: list, key) -> bool:
    for char in group:
        if(char == key):
            return True
    return False
 
badgeList = []
group = [] 
groupSize = 3

with open("day_3\script_3_values.txt") as file:
    for line in file:
        line_list = list(line)
        group.append(line_list)
        if(len(group) == groupSize): #Create a new group, if the current one is full
            badgeList.append(findBadge(group))
            group = list()
        
sumKeyPriority = 0
for badge in badgeList:
    sumKeyPriority+=priorityString.find(badge)
print("Solution 2)", sumKeyPriority)
