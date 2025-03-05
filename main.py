import numpy as np


def add_borders(matrix, object_positions, color):
    rows, cols = len(matrix), len(matrix[0])
    new_matrix = np.array(matrix)  # Copy input matrix

    # Find the bounding box of the given object
    min_r = min(p[0] for p in object_positions)
    max_r = max(p[0] for p in object_positions)
    min_c = min(p[1] for p in object_positions)
    max_c = max(p[1] for p in object_positions)

    print(min_r, max_r, min_c, max_c)

    # Add a border (value 9) around the bounding box
    for r in range(min_r - 1, max_r + 2):
        for c in range(min_c - 1, max_c + 2):
            if (r, c) not in object_positions and 0 <= r < rows and 0 <= c < cols:
                new_matrix[r][c] = color

    return new_matrix.tolist()



# Example matrix (empty grid)
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Define object positions (the 4x4 square)
obj_positions = [(1,1), (1,2), (1,3), (1,4), (2,1), (2,2), (2,3), (2,4), (3,1), (3,2), (3,3), (3,4)]

# Run border function
bordered_matrix = add_borders(matrix, obj_positions, 9)
print("input", matrix)
print("output", bordered_matrix)
