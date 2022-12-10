def executeTask(knotsAmount:int) -> int:
    with open("day_9/script_9_values.txt") as file:
        knotsAmount = knotsAmount
        knots = []
        for k in range(0, knotsAmount, 1):
           knots.append([0,0])
        tailPositions = set()
        
        for line in file:

            dirChar, dist = line.split(" ")
            dist = int(dist)
            moveX = 0 
            moveY = 0

            #Direction
            if(dirChar == 'U'):
                moveY=-1
            if(dirChar == 'D'):
                moveY=1
            if(dirChar == 'R'):
                moveX=1
            if(dirChar == 'L'):
                moveX=-1

            for i in range(0, dist, 1):
                knots[0][0]+=moveX
                knots[0][1]+=moveY
                for t in range(1, len(knots), 1):
                    diffX=knots[t-1][0]-knots[t][0]
                    diffY=knots[t-1][1]-knots[t][1]
                    if(abs(diffX) > 1 and abs(diffY) > 0
                    or abs(diffY) > 1 and abs(diffX) > 0):
                        knots[t][0]+= 1 if diffX > 0 else -1
                        knots[t][1]+= 1 if diffY > 0 else -1
                    elif(diffX >= 2 or diffX <= -2):
                        knots[t][0]+= 1 if diffX > 0 else -1
                    elif(diffY >= 2 or diffY <= -2):
                        knots[t][1]+= 1 if diffY > 0 else -1

                    tailPositions.add(str(knots[len(knots)-1]))
        return len(tailPositions)

print("Solution 1) ", executeTask(2))
print("Solution 2) ", executeTask(10))