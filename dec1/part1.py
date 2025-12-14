
filename = "input.txt"



with open(filename) as f:
    data = f.read()

zeroes = 0

count = 50

for row in data.split("\n"):
    if row[0] == "L":
        count -= int(row[1:])
    elif row[0] == "R":
        count += int(row[1:])
    if count%100 == 0:
        zeroes += 1

print(zeroes)

