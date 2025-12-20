import math


filename = "input.txt"



with open(filename) as f:
    data = f.read()



data = data.split("\n")[:-1]



beams = {data[0].index("S")}


splits = 0

for row in data[2::2]:

    print(row)
    to_be_removed = set()
    to_be_added   = set()
    for i in beams:
        if row[i] == "^":
            to_be_added |= {i-1, i+1}
            to_be_removed |= {i}
            splits += 1
    beams = (beams | to_be_added) - to_be_removed

print(splits)
