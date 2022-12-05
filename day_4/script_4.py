groupList = []
group = []
fully_overlap = 0
partially_overlap = 0
with open("day_4\script_4_values.txt") as file:
    for line in file:
        group = line.split(sep=",")
        #Remove \n
        group[1] = group[1][0:len(group[1])-1]
        #Split values into two
        group[0] = group[0].split(sep="-")
        group[1] = group[1].split(sep="-")
        #Check if one pair fully overlaps with the other
        if((int(group[0][0]) >= int(group[1][0]) and int(group[0][1]) <= int(group[1][1]))
        or (int(group[1][0]) >= int(group[0][0]) and int(group[1][1]) <= int(group[0][1]))):
            fully_overlap+=1

        if(int(group[0][0]) >= int(group[1][0]) and int(group[0][0]) <= int(group[1][1]) 
        or int(group[1][0]) >= int(group[0][0]) and int(group[1][0]) <= int(group[0][1]) 
        or int(group[0][1]) >= int(group[1][0]) and int(group[0][1]) <= int(group[1][1])
        or int(group[1][1]) >= int(group[0][0]) and int(group[1][1]) <= int(group[0][1])):        
            partially_overlap+=1

print("Solution 1 )", fully_overlap)
print("Solution 2 )", partially_overlap)