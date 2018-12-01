data = [int(line.strip()) for line in open("day01input.txt", "r").read().split()]

#Part 1
print(sum(data))

#Part 2
used = set([0])
f = 0
while True:
    for d in data:
        f += d
        if f in used:
            print(f)
            exit()
        used.add(f)

