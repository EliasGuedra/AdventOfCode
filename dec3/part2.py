
filename = "input.txt"


with open(filename) as f:
    data = f.read()

s = 0

for row in data[:-1].split("\n"):
    print(row)
    current_index = -1


    for i in range(11):
        next_digit = max([int(i) for i in row[current_index+1:-11+i]])

        current_index = row.index(str(next_digit), current_index+1)
         
        s += next_digit * 10**(11-i)

        print(next_digit * 10**(11-i))

    
    last_digit = max([int(i) for i in row[current_index+1:]])

    print(last_digit)
    s += last_digit 


print(s)
