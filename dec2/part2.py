
filename = "input.txt"



with open(filename) as f:
    data = f.read()


ranges = data.split(',')

s = 0 


def check_string(string, k):
    if len(string) % k != 0:
        return False 

    pattern = string[:k]
    for m in range(0,  len(string)//k):
        if pattern != string[m*k:(m+1)*k]:
            return False
    return True




for r in ranges:
    l, u = r.split("-")

    for i in range(int(l), int(u)):
        string = str(i)
        for k in range(1, len(string)//2 + 1):
            if check_string(string, k):
                print(string, k)
                s += i
                break
print(s)
