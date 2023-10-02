from DirectionsFuncs import *
from printPathsFunc import *

# findallpaths function performs backtrack technique to find all possible paths from start point to goal point
# by passing each direction if possible until find the goal point or find stone and then will back to find out another path

def FindAllPaths(maze,path,end):
    LastValue = path[len(path)-1]
    if LastValue == end:
        printdirections(path)
        return
    
    if isDownallowed(path,maze,LastValue):
        path.append([LastValue[0]+1,LastValue[1]])
        FindAllPaths(maze,path,end)
        path.pop()

    if isUpallowed(path,maze,LastValue):
        path.append([LastValue[0]-1,LastValue[1]])
        FindAllPaths(maze,path,end)
        path.pop()
    
    if isRightallowed(path,maze,LastValue):
        path.append([LastValue[0],LastValue[1]+1])
        FindAllPaths(maze,path,end)
        path.pop()
    
    if isLeftallowed(path,maze,LastValue):
        path.append([LastValue[0],LastValue[1]-1])
        FindAllPaths(maze,path,end)
        path.pop()


