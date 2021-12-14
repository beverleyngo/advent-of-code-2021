import numpy as np

# Write coordinates to a list of lists
coordinates = []
with open('day5_input.txt', 'r') as f:
    for line in f:
        coords = line.split(' -> ')
        coord_a = coords[0].split(',')
        coord_b = coords[1].split(',')
        coord_a = [int(coord) for coord in coord_a]
        coord_b = [int(coord) for coord in coord_b]
        coordinates.append([coord_a, coord_b])

# Function to remove non-eligible coordinates (non-horizontal or non-vertical lines)
def remove_coords(coordinates):
    new_coords = []
    for i in range(len(coordinates)):
        coord = coordinates[i]
        if (coord[0][0] == coord[1][0]) or (coord[0][1] == coord[1][1]):
            new_coords.append(coord)
    return new_coords

# Function to create a grid for size of coordinates
def create_grid(coordinates):
    grid = []
    maximum = np.max(coordinates) + 1
    for i in range(maximum):
        grid.append([0] * maximum)
    return grid

# Function to +1 to each gridspace if a line passes through it
def drawlines(coordinates, grid):
    for coordinate in coordinates:
        if coordinate[0][0] == coordinate[1][0]:
            column = coordinate[0][0]
            first_row = coordinate[0][1]
            last_row = coordinate[1][1]
            if first_row > last_row:
                for row in range(last_row, first_row+1):
                    grid[row][column] += 1
            elif first_row < last_row:
                for row in range(first_row, last_row+1):
                    grid[row][column] += 1
        if coordinate[0][1] == coordinate[1][1]:
            row = coordinate[0][1]
            first_column = coordinate[0][0]
            last_column = coordinate [1][0]
            if first_column > last_column:
                for column in range(last_column, first_column+1):
                    grid[row][column] += 1
            elif first_column < last_column:
                for column in range(first_column, last_column+1):
                    grid[row][column] += 1     
    return grid

# Function to count how many grid spaces are overlapped at least twice
def count_overlaps(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] >= 2:
                count += 1
    return count

new_coords = remove_coords(coordinates)
grid = create_grid(new_coords)
new_grid = drawlines(new_coords,grid)
print(count_overlaps(new_grid))