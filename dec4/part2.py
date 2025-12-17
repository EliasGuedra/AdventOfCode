
import numpy as np

filename = "input.txt"



with open(filename) as f:
    data = f.read()


data = data.split("\n")[:-1]

width = len(data[0])
height = len(data)



matrix = []

for row in data:
    row = row.replace("@", "1")
    row = row.replace(".", "0")
    row = [int (i) for i in row]
    matrix.append(row)


matrix = np.array(matrix)

s = 0

last_s = -1

while s != last_s:
    last_s = s
    for x in range(width):
        for y in range(height):
            if matrix[x,y] == 1 and matrix[max(x-1, 0) :min(x+2,width), max(y-1,0):min(y+2,height)].sum()< 5:
                matrix[x, y] = 0
                s += 1


print(s)
