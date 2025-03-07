from type import Grid

# Copy grid
def copy_grid(grid: Grid) -> Grid:
    return [row[:] for row in grid]
