# backtracking-maze-solver

This application is programmed to find all possible paths that lead from the start point to the goal point in a given maze and  
The program uses the backtracking technique to deep into this maze beginning with the start point and search for the goal point and back again to find out another path. 
The backtracking technique goes deep into three directions and doesn't count the direction it came from to avoid infinite looping. 
If the backtracking technique finds a wall in front of it, it will also backtrack and discover another path. 
After finding all paths as indices of the maze, the program prints directions instead of these indices to be obviously clear.

## Functions

The following functions are used in this program:

### `printdirections(path)`

This function prints all paths indices of the maze that lead from the start point to the goal point by its names (right, left, up, and down).

### `isDownallowed(path,maze,LastValue)`

This function checks if it's possible for the backtracking technique to go deeper in down direction.

### `isUpallowed(path,maze,LastValue)`

This function checks if it's possible for the backtracking technique to go deeper in up direction.

### `isRightallowed(path,maze,LastValue)`

This function checks if it's possible for the backtracking technique to go deeper in right direction.

## Usage

To use this program, you need to provide a maze as a 2-D list of strings. Each string represents a single space or position of the maze. The walls are represented by '*'.

