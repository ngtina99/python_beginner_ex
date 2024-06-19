number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])

for row in number_grid:
    print(row) # every element

for row in number_grid:
    for col in row: # everything inside one by one
        print(col)