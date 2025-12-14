
filename = "input.txt"



with open(filename) as f:
    data = f.read()


ranges = data.split(',')

s = 0 

for r in ranges:
    l, u = r.split("-")

    for i in range(int(l), int(u)):
        string = str(i)
        if string[:len(string)//2] == string[len(string)//2:]:
            s += i

print(s)
