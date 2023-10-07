class Maze:
    # Initializes the maze by taking user input for the size of the maze and creating a 2D list of empty spaces.
    def __init__(self):
        while True:
            # Takes user input for the size of the maze.
            self.MazeSize = int(input("Enter maze size: "))
            # If the size of the maze is greater than 2, break out of the loop.
            if self.MazeSize>2:
                break
        # Creates a 2D list of empty spaces.
        self.maze = [[" "]*self.MazeSize for row in range(self.MazeSize)]
    
    # Takes user input for the number of obstacles and their positions in the maze.
    def FillObstacles(self):
        self.PrintMaze()
        while True:
            NumObstacles = int(input("Enter number of obstacles: "))
            if NumObstacles>=0:
                break
        for obstacle in range(NumObstacles):
            while True:
                x = int(input(f"Enter X-axis for Obstacle number {obstacle+1}: "))
                y = int(input(f"Enter Y-axis for Obstacle number {obstacle+1}: "))
                # If both X-axis and Y-axis are within bounds and there is no obstacle at that position, place an obstacle at that position.
                if x>0 and x<=self.MazeSize and y>0 and y<=self.MazeSize and self.maze[x-1][y-1]!="*":
                    self.maze[x-1][y-1]="*"
                    self.PrintMaze()
                    break

    # Prints the maze
    def PrintMaze(self):
        print()
        print("--------"*self.MazeSize+"-"*(1+self.MazeSize))
        for i in range(self.MazeSize):
            print("| ",end="")
            for j in range(self.MazeSize):
                print(f"   {self.maze[i][j]}  " if self.maze[i][j]!=" " else f"{i+1,j+1}",end = ' | ')
            print()
            print("--------"*self.MazeSize+"-"*(1+self.MazeSize))
        print()