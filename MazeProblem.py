
'''
- this application programmed to find all possible paths that lead from start point to goal point in a given maze

'''

from MazeSolver import *
from MazeCreation import *

maze = Maze()
maze.FillObstacles()

solver = Solver()
start=[0,0]
end=[3,3]
solver.FindAllPaths(maze,list(start),end)
solver.PrintPaths()

