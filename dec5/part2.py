
filename = "input.txt"



with open(filename) as f:
    data = f.read()





ranges, indecies = data[:-1].split("\n\n")

ranges = ranges.split("\n")


ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges]


ranges.sort(key=lambda r: r[0])


l = ranges[0][0]
u = ranges[0][1]

s = 0

for i in range(len(ranges)):
    if ranges[i][0] > u:
        s += u-l + 1
        l = ranges[i][0]
        u = ranges[i][1]
    else:
        u = max(u, ranges[i][1])

s += u-l + 1 


