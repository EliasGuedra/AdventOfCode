from functools import lru_cache


filename = "input.txt"

with open(filename) as f:
    data = f.read()

data = data.split("\n")[:-1]

@lru_cache(None)
def traverse(row, col):

    if row >= len(data)-1:
        return 0

    if col < 0 or col >= len(data[row + 1]):
        return 0

    if data[row + 1][col] == "^":
        return (
            traverse(row + 1, col - 1) +
            traverse(row + 1, col + 1) + 1
        )
    else:
        return traverse(row + 1, col)
    

start_col = data[0].index("S")

splits = traverse(0, start_col)

print(splits+1)
