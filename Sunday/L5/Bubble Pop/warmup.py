# A simple 2D grid
grid = [
    ["T", ".", ".", "T"],
    [".", "T", ".", "."],
    ["T", "T", ".", "."],
]

tree_count = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == "T":
            tree_count += 1

print(f"There are {tree_count} trees.")


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)