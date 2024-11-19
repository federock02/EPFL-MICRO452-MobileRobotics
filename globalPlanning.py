import numpy as np
import matplotlib.pyplot as plt

class GlobalPlanning:
    def __inite__(self):
        self.magnification = 5
        self.map = []
        self.start = []
        self.goal = []
        self.path = [] #Shortest path
        
    #here is the function for the dijkstra algortihm
    def dijkstra(self, matrix, start, goal):
        #If current goal equal old goal we don't do the algorithm
        #if self.goal == goal:
            #return self.path
            
        # Initialize variables
        n = 0  # Distance from start
        grid = np.full_like(matrix, -4)  # Initialize grid with -4 (unmarked)
        current = None  # Current cell in path
        path = []

        # Make obstacles bigger
        obstacles = []
        for x in range(grid.shape[0]):
            for y in range(grid.shape[1]):
                if matrix[x, y] == -1:
                    obstacles.append((x, y))
        for obstacle in obstacles:
            if matrix[obstacle[0]-1, obstacle[1]] == 0:
                for x in range(5):
                    if 0 <= obstacle[0] - x:
                        matrix[obstacle[0] - x, obstacle[1]] = -1
            if matrix[obstacle[0]+1, obstacle[1]] == 0:
                for x in range(5):
                    if obstacle[0] + x < grid.shape[0]:
                        matrix[obstacle[0] + x, obstacle[1]] = -1
            if matrix[obstacle[0], obstacle[1]-1] == 0:
                for y in range(5):
                    if 0 <= obstacle[1] - y:
                        matrix[obstacle[0], obstacle[1] - y] = -1
            if matrix[obstacle[0], obstacle[1]+1] == 0:
                 for y in range(5):
                    if obstacle[1] + y <= grid.shape[1]:
                        matrix[obstacle[0], obstacle[1] + y] = -1
                
        # Mark the start cell with n
        grid[start] = n
    
        # Initialize a list to keep track of the frontier cells
        frontier = [start]
    
        while grid[goal] == -4:
            n += 1
            new_frontier = []
            # For each cell in the current frontier
            for cell in frontier:
                # Get neighbors of the cell (up, down, left, right)
                neighbors = [
                    (cell[0]-1, cell[1]),  # Up
                    (cell[0]+1, cell[1]),  # Down
                    (cell[0], cell[1]-1),  # Left
                    (cell[0], cell[1]+1)   # Right
                ]
                for neighbor in neighbors:
                    # Check if neighbor is within bounds and 
                    if (0 <= neighbor[0] < grid.shape[0]) and (0 <= neighbor[1] < grid.shape[1]):# Check if neighbor is within bounds
                        if grid[neighbor] == -4: # Unmarked cell  
                            if matrix[neighbor] != -1: # Not an obstacle
                                # Mark neighbor with n
                                grid[neighbor] = n
                                # Add neighbor to new frontier
                                new_frontier.append(neighbor)
            if not new_frontier:
                # No more cells to explore, and goal is unreachable
                return None, matrix
            frontier = new_frontier
    
        # Reconstruct the path
        current = goal
        path.append(current)
        while current != start:
            neighbors = [
                (current[0]-1, current[1]),  # Up
                (current[0]+1, current[1]),  # Down
                (current[0], current[1]-1),  # Left
                (current[0], current[1]+1)   # Right
            ]
            # Find the neighbor with the lowest mark (n value)
            min_n = grid[current]
            next_cell = None
            for neighbor in neighbors:
                if (0 <= neighbor[0] < grid.shape[0]) and (0 <= neighbor[1] < grid.shape[1]): 
                    if grid[neighbor] >= 0 and grid[neighbor] < min_n:
                        min_n = grid[neighbor]
                        next_cell = neighbor
                        
            if next_cell is None:
                # No path found
                return None, matrix
            # Append next_cell to path
            path.append(next_cell)
            current = next_cell
        # Reverse the path
        path.reverse()
        return path, matrix