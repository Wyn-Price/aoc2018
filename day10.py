import re
data = [list(map(int, re.findall(r"position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>", line)[0])) for line in open("day10input.txt").read().splitlines()]
dist = 99999999
time = 0
while True:
    xp = []
    yp = []
    for d in data:
        d[0] = d[0] + d[2]
        d[1] = d[1] + d[3]
        xp.append(d[0])
        yp.append(d[1])
    testdist = max(xp) - min(xp) + max(yp) - min(yp)
    if testdist > dist:
        for d in data:
            d[0] = d[0] - d[2]
            d[1] = d[1] - d[3]
        break; #Exit loop
    else:
        dist = testdist
    time+=1


outdata = ""

outx = [x for (x, y, vx, vy) in data]
outy = [y for (x, y, vx, vy) in data]

pos = [(x, y) for (x, y, vx, vy) in data]

for y in range(min(outy) - 1, max(outy) + 1):
    for x in range(min(outx) - 1, max(outx) + 1):
        if (x, y) in pos:
            outdata += "#"
        else:
            outdata += " "
    outdata += "\n"

print(outdata)
print(time)






