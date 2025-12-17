
filename = "input.txt"



with open(filename) as f:
    data = f.read()





ranges, indecies = data[:-1].split("\n\n")

ranges = ranges.split("\n")
indecies = indecies.split("\n")

s = 0

for index in indecies:
    for r in ranges:
        print(r)
        l, u = r.split("-")
        if int(index) >= int(l) and int(index) <= int(u):
            s += 1
            break

print(s) 
