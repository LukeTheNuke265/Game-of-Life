# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 21:19:32 2024

@author: lukas
"""
#GAME of life 
'''

Rules: 
    
    The Game of Life is a cellular automaton devised by mathematician John Conway, consisting of a grid of cells,
    where each cell can be either alive (1) or dead (0). 
    The grid evolves over discrete time steps according to a set of rules applied to each cell based on its eight
    neighbors. The rules are:

Underpopulation: A live cell with fewer than two live neighbors dies (becomes dead). 
This occurs due to underpopulation.

Survival: A live cell with two or three live neighbors remains alive (survives to the next generation).

Overpopulation: A live cell with more than three live neighbors dies (becomes dead). 
This occurs due to overpopulation.

Reproduction: A dead cell with exactly three live neighbors becomes alive (reproduction).

'''


'''

SETUP 

Initialize Grid: Set up the initial configuration of cells.
Display Grid: Show the initial grid on the screen.
While True Loop: Keep updating the grid in a loop until the simulation is manually stopped.
Update Grid: Apply the rules to each cell based on its neighbors and compute the next state.
Display Updated Grid: Show the updated grid state.
Pause: Wait for a short period before updating the grid again to control the simulation speed.

Stop the simulation with Ctrl+C

ENJOY!
'''



import numpy as np
import matplotlib.pyplot as plt

# Define the size of the grid
GRID_SIZE = 100 #Change to set more complex systems
UPDATE_INTERVAL = 0.01  #Smaller value = Faster update speed

def initialize_grid(size):
    """Initialize the grid with random values."""
    return np.random.choice([0, 1], size=(size, size))

def update_grid(grid):
    new_grid = np.copy(grid)
    rows, cols = grid.shape
    for i in range(rows):
        for j in range(cols):
            # Count the number of live neighbors
            num_live_neighbors = np.sum(grid[max(i-1,0):min(i+2,rows), max(j-1,0):min(j+2,cols)]) - grid[i, j]
            
            if grid[i, j] == 1 and (num_live_neighbors < 2 or num_live_neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and num_live_neighbors == 3:
                new_grid[i, j] = 1
                
    return new_grid


grid = initialize_grid(GRID_SIZE)

plt.ion()
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap='binary')
ax.set_title('Game of Life')
plt.axis('off')



try:
    while True:
        # GRid update
        grid = update_grid(grid)
        
        # Plot update
        mat.set_data(grid)
        plt.draw()  
        plt.pause(UPDATE_INTERVAL) 
        plt.clf()  
        ax = plt.gca() 
        mat = ax.matshow(grid, cmap='binary') 
        plt.axis('off')
        
except KeyboardInterrupt:
    #Stop the simulation with Ctrl+C
    print("Simulation stopped.")

