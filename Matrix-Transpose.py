# Matrix at the start
grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

# Number of rows and columns as variables
rows = len(grid)
cols = len(grid[0])

# Create matrix transpose function
def transpose(matrix):
    for i in range(cols):
        for j in range(rows):
            print(matrix[j][i], end='')
        if i + 1 < cols:
            print()

# Call function on this matrix
transpose(grid)
