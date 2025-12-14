
filename = "input.txt"



with open(filename) as f:
    data = f.read()


s = 0

for row in data[:-1].split("\n"):
    first_digit = max([int(i) for i in row[:-1]])
    first_index = row.index(str(first_digit))

    second_digit = max([int(i) for i in row[1+first_index:]])
    
    s += 10*int(first_digit) + int(second_digit)

    print(row)
    print(first_digit, second_digit)

print(s)
