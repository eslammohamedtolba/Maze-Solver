
'''
- directions functions that allow backtracking technique to move in that directions 
- if satisfied some conditions in each direction such as:
        (1) moving in this direction will not get us out of the maze 
        (2) backtracking technique doesn't count one of the directions which came from to avoid infinity looping
        (3) direction is not a wall  
'''

# check if it's possible for backtrack technique to go deepen in down direction in the maze
def isDownallowed(path,maze,LastValue):
    if LastValue[0]+1<len(maze) and path.count([LastValue[0]+1,LastValue[1]])==0 and maze[LastValue[0]+1][LastValue[1]]!="*":
        return True
    return False


# check if it's possible for backtrack technique to go deepen in up direction in the maze
def isUpallowed(path,maze,LastValue):
    if LastValue[0]-1>=0 and path.count([LastValue[0]-1,LastValue[1]])==0 and maze[LastValue[0]-1][LastValue[1]]!="*":
        return True
    return False


# check if it's possible for backtrack technique to go deepen in right direction in the maze
def isRightallowed(path,maze,LastValue):
    if LastValue[1]+1<len(maze) and path.count([LastValue[0],LastValue[1]+1])==0 and maze[LastValue[0]][LastValue[1]+1]!="*":
        return True
    return False


# check if it's possible for backtrack technique to go deepen in left direction in the maze
def isLeftallowed(path,maze,LastValue):
    if LastValue[1]-1>=0 and path.count([LastValue[0],LastValue[1]-1])==0 and maze[LastValue[0]][LastValue[1]-1]!="*":
        return True
    return False

