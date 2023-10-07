"""
- Solver uses backtrack technique to deep into this maze begining with start point and search about goal point and back again to find out another path 
- the direction we go will not get us out of the maze and not the direction that came from to avoid infinity looping and is not a wall
- after finding all paths as indices of the maze, program prints dirctions instead of this indices to be obviously clear 
"""
from copy import deepcopy



class Solver:
    def __init__(self):
        self.paths = []
    '''
    - directions functions that allow backtracking technique to move in that directions 
    - if satisfied some conditions in each direction such as:  
    '''
    # check if it's possible for backtrack technique to go deepen in down direction in the maze
    def isDownallowed(self,path,maze,LastValue):
        if LastValue[0]+1<len(maze) and path.count([LastValue[0]+1,LastValue[1]])==0 and maze[LastValue[0]+1][LastValue[1]]!="*":
            return True
        return False

    # check if it's possible for backtrack technique to go deepen in up direction in the maze
    def isUpallowed(self,path,maze,LastValue):
        if LastValue[0]-1>=0 and path.count([LastValue[0]-1,LastValue[1]])==0 and maze[LastValue[0]-1][LastValue[1]]!="*":
            return True
        return False

    # check if it's possible for backtrack technique to go deepen in right direction in the maze
    def isRightallowed(self,path,maze,LastValue):
        if LastValue[1]+1<len(maze) and path.count([LastValue[0],LastValue[1]+1])==0 and maze[LastValue[0]][LastValue[1]+1]!="*":
            return True
        return False

    # check if it's possible for backtrack technique to go deepen in left direction in the maze
    def isLeftallowed(self,path,maze,LastValue):
        if LastValue[1]-1>=0 and path.count([LastValue[0],LastValue[1]-1])==0 and maze[LastValue[0]][LastValue[1]-1]!="*":
            return True
        return False

    # findallpaths function performs backtrack technique to find all possible paths from start point to goal point
    # by passing each direction if possible until find the goal point or find stone and then will back to find out another path
    def FindAllPaths(self,Maze,path,end):
        LastValue = path[len(path)-1]
        if LastValue == end:
            self.paths.append(deepcopy(path))
            return
        if self.isDownallowed(path,Maze.maze,LastValue):
            path.append([LastValue[0]+1,LastValue[1]])
            self.FindAllPaths(Maze,path,end)
            path.pop()

        if self.isUpallowed(path,Maze.maze,LastValue):
            path.append([LastValue[0]-1,LastValue[1]])
            self.FindAllPaths(Maze,path,end)
            path.pop()
        
        if self.isRightallowed(path,Maze.maze,LastValue):
            path.append([LastValue[0],LastValue[1]+1])
            self.FindAllPaths(Maze,path,end)
            path.pop()
        
        if self.isLeftallowed(path,Maze.maze,LastValue):
            path.append([LastValue[0],LastValue[1]-1])
            self.FindAllPaths(Maze,path,end)
            path.pop()
    
    # printing all paths indices of the maze that lead from start point to goal point by its names (right,left,up and down)
    def PrintPaths(self):
        for path in self.paths:
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
