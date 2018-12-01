with open('day01/p01_input.txt') as f:
    result = 0
    for line in f.readlines():
        if line[0] == '+':
            result += int(line[1:])
            continue
        result -= int(line[1:])

print(result)