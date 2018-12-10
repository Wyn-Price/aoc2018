dataraw = [line for line in open("day10input.txt").read().splitlines()]
data = []

for d in dataraw: #Imagine useing regex. This meme was made by split gang
    data.append([int(d.split("<")[1].split(",")[0]), int(d.split(">")[0].split()[-1]),
                 int(d.split("<")[2].split(",")[0]), int(d.split(">")[1].split()[-1])])

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
    xa = sum(xp) / len(xp)
    ya = sum(yp) / len(yp)

    testdist = 0
    for d in data:
        testdist += abs(d[0] - xa) + abs(d[1] - ya)
    if testdist > dist:
        for d in data:
            d[0] = d[0] - d[2]
            d[1] = d[1] - d[3]
        break;
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






