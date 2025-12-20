
filename = "input.txt"

with open(filename) as f:
    data = f.read()

data = data.split("\n")[:-1]


visited = {}

def traverse(row, col):

    if cached_val := visited.get((row,col), False):
        return cached_val

    if row >= len(data)-1:
        visited[(row, col)] = 0
        return 0

    if col < 0 or col >= len(data[row + 1]):
        return 0

    if data[row + 1][col] == "^":

        visited[(row, col)] = traverse(row + 1, col - 1) + traverse(row + 1, col + 1) + 1
        return visited[(row, col)]
    else:
        visited[(row, col)] = traverse(row + 1, col)
        return visited[(row, col)]

start_col = data[0].index("S")

splits = traverse(0, start_col)

print(splits+1)
