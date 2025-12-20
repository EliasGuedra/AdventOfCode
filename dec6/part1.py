import math

filename = "input.txt"

with open(filename) as f:
    data = f.read()

data = data.split("\n")[:-1]
data = [s.split() for s in data]

s = 0

for i, operator in enumerate(data[-1]):
    if operator == "+":
        s += sum([int(row[i]) for row in data[:-1]])
    elif operator == "*":
        s += math.prod([int(row[i]) for row in data[:-1]])

print(s)
