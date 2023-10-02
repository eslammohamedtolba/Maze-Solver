
# printing all paths indices of the maze that lead from start point to goal point by its names (right,left,up and down)
def printdirections(path):
    for dir in range(1,len(path)):
        if [path[dir][0]-path[dir-1][0],path[dir][1]-path[dir-1][1]] == [1,0]:
            print("down",end = " ")
        elif [path[dir][0]-path[dir-1][0],path[dir][1]-path[dir-1][1]] == [-1,0]:
            print("up",end=" ")
        elif [path[dir][0]-path[dir-1][0],path[dir][1]-path[dir-1][1]] == [0,1]:
            print("right",end=" ")
        else:
            print("left",end=" ")
    print()