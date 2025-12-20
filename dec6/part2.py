filename = "input.txt"

with open(filename) as f:
    data = f.read()

data = data.split("\n")[:-1]

def get_column_number(data, i):
    column = ""
    for row in data:
        if row[i] != " ":
            column += row[i]
    
    if column == "":
        return -1
    return int(column)

s = 0

current_value = 0
current_operator = "+"

for i, operator in enumerate(data[-1]):
    
        if (current_column := get_column_number(data[:-1], i)) == -1: 
        s += current_value
        print("Adding:", current_value)
        continue
    if operator == " ":
        if current_operator == "+":
            current_value += current_column
        elif current_operator == "*":
            current_value *= current_column


    if operator == "+":
        current_operator = "+"
        current_value = current_column
    elif operator == "*":
        current_operator = "*"
        current_value = current_column

    print(current_column)
print(s)

