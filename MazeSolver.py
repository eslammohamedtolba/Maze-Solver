
'''
- this application programmed to find all possible paths that lead from start point to goal point in a given maze
- using backtrack technique to deep into this maze begining with start point and search about goal point and back again to find out another path 
- backtracking technique goes deepen into three directions and doesn't count the direction it came from to avoid infinity looping
- if backtrack technique finds wall in front of it then will back and discover another path 
- after finding all paths as indices of the maze, program prints dirctions instead of this indices to be obviously clear 
'''

from AllPathsFunc import *



maze = [["","","*",""],
        ["*","","",""],
        ["","","","*"],
        ["","*","",""]]

start=[0,0],
end=[3,3]
FindAllPaths(maze,list(start),end)

