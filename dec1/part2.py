
filename = "input.txt"



with open(filename) as f:
    data = f.read()

zeroes = 0

count = 50

for row in data.split("\n"):
    if row[0] == "L":
        sign = -1
    elif row[0] == "R":
        sign = 1
    
    add = int(row[1:])
    
    for _ in range(add):
        count+=sign
        if count%100==0:
            zeroes+=1

print(zeroes)




