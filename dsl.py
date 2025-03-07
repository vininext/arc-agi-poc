from typing import List
from helper import copy_grid
from type import Color, Coordinates, Grid

def add_border(grid: Grid, coordinates: Coordinates, color: Color) -> Grid:
    """
    Add a border of specified color around a set of coordinates in a grid.
    Task: 4258a5f9
    """
    rows, cols = len(grid), len(grid[0])
    new_grid = copy_grid(grid)

    min_r = min(p[0] for p in coordinates)
    max_r = max(p[0] for p in coordinates)
    min_c = min(p[1] for p in coordinates)
    max_c = max(p[1] for p in coordinates)    

    for r in range(min_r - 1, max_r + 2):
        for c in range(min_c - 1, max_c + 2):
            if (r, c) not in coordinates and 0 <= r < rows and 0 <= c < cols:
                new_grid[r][c] = color

    return new_grid

def change_color(grid: Grid, coordinates: Coordinates, color: Color) -> Grid:
    """
    Change the color of a set of coordinates in a grid.    
    """
    new_grid = copy_grid(grid)
    for r, c in coordinates:
        new_grid[r][c] = color
    return new_grid

def replace_color(grid: Grid, color_from: Color, color_to: Color) -> Grid:
    """
    Replace the color of a set of coordinates in a grid.
    Tasks: c8f0f002
    """
    return [[color_to if cell == color_from else cell for cell in row] for row in grid]
    
def connect_horizontal(grid: Grid, coordinates: Coordinates, color: Color) -> Grid:
    """
    Connect horizontal lines in a grid with a specified color.
    Tasks: a699fb00
    """
    new_grid = copy_grid(grid)
    for r, c in coordinates:
        if c + 2 < len(new_grid[r]) and new_grid[r][c+1] == 0 and new_grid[r][c+2] != 0:
            new_grid[r][c+1] = color            
    return new_grid

def Fill8(grid: Grid, color: Color):
    """
    Changes the color of the interior of an object while preserving the border.
    ""
    rows = len(grid)
    cols = len(grid[0])
    
    new_grid = copy_grid(grid)
    
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            current = grid[i][j]
            if (1 <= current <= 9 and
                grid[i-1][j] == current and      # North
                grid[i+1][j] == current and      # South
                grid[i][j-1] == current and      # West
                grid[i][j+1] == current and      # East
                grid[i-1][j-1] == current and    # Northwest
                grid[i-1][j+1] == current and    # Northeast
                grid[i+1][j-1] == current and    # Southwest
                grid[i+1][j+1] == current):      # Southeast
                new_grid[i][j] = color
                
    return new_grid

    
        

