
points_for_win = 6
points_for_tie = 3
points_for_lose = 0
score = 0

def calculateScore(line_string: str, score: int) -> int:
    #Berechnen der Punkte

    if(line_string[0] == "A"): # ROCK
        if(line_string[2] == "Z"): #Sciss LOSE
            shape_points = 3
            score += shape_points + points_for_lose
        if(line_string[2] == "X"): #ROCK TIE
            shape_points = 1
            score += shape_points + points_for_tie
        if(line_string[2] == "Y"): #PAPER WIN
            shape_points = 2
            score += shape_points + points_for_win

    if(line_string[0] == "B"): # PAPER
        if(line_string[2] == "X"): #ROCK LOSE
            shape_points = 1
            score += shape_points + points_for_lose
        if(line_string[2] == "Y"): #PAPER TIE
            shape_points = 2
            score += shape_points + points_for_tie
        if(line_string[2] == "Z"): #SCISS WIN
            shape_points = 3
            score += shape_points + points_for_win

    if(line_string[0] == "C"): # SCISS
        if(line_string[2] == "Y"): #PAPER LOSE
            shape_points = 2
            score += shape_points + points_for_lose
        if(line_string[2] == "Z"): #SCISS TIE
            shape_points = 3
            score += shape_points + points_for_tie
        if(line_string[2] == "X"): #ROCK WIN
            shape_points = 1
            score += shape_points + points_for_win
    
    return score

### Task 1

line_string = ""
with open("day_2\script_2_values.txt") as file:
    for line in file:
        line_string = list(line)
        score = calculateScore(line_string, score)
print("Solution 1)", score)


### Task 2

score = 0
with open("day_2\script_2_values.txt") as file:
    for line in file:

        line_string = list(line)

        #Ändern der Werte passend zu den Konditionen

        if(line_string[2] == "X"): #LOSE
            if(line_string[0] == "A"):
                line_string[2] = "Z"
            if(line_string[0] == "B"):
                line_string[2] = "X"
            if(line_string[0] == "C"):
                line_string[2] = "Y"

        elif(line_string[2] == "Y"): #TIE
            if(line_string[0] == "A"):
                line_string[2] = "X"
            if(line_string[0] == "B"):
                line_string[2] = "Y"
            if(line_string[0] == "C"):
                line_string[2] = "Z"
        
        elif(line_string[2] == "Z"): #WIN
            if(line_string[0] == "A"):
                line_string[2] = "Y"
            if(line_string[0] == "B"):
                line_string[2] = "Z"
            if(line_string[0] == "C"):
                line_string[2] = "X"

        score = calculateScore(line_string, score)

print("Solution 2)", score)

