data = open("day03input.txt", "r").read().split("\n")

#Part 1
lis = set()
used = set()
ma = {}
count = 0
for line in data:
    exec("offset = " + line.split("@ ")[1].split(":")[0])
    xs = int(line.split(": ")[1].split("x")[0])
    ys = int(line.split(": ")[1].split("x")[1])
    for x in range(xs):
        for y in range(ys):
            pos = (offset[0] + x, offset[1] + y)
            if pos not in ma:
                ma[pos] = 1
            else:
                ma[pos] = ma[pos] + 1
            if pos not in lis:
                lis.add(pos)
            elif pos not in used:
                count += 1
                used.add(pos)

print(count)

#Part 2
for line in data:
    exec("offset = " + line.split("@ ")[1].split(":")[0])
    xs = int(line.split(": ")[1].split("x")[0])
    ys = int(line.split(": ")[1].split("x")[1])
    new = False;
    for x in range(xs):
        for y in range(ys):
            pos = (offset[0] + x, offset[1] + y)
            if ma[pos] > 1:
                new = True
                break
        if new:
            break;
    if not new:
        print(line)
