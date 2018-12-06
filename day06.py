points = list((int(s.split(",")[0]), int(s.split(" ")[1])) for s in open("day06input.txt", "r").read().splitlines())

mi = (min(p[0] for p in points), min(p[1] for p in points))
ma = (max(p[0] for p in points), max(p[1] for p in points))

data = {}

for x in range(ma[0] - mi[0] + 1):
    x += mi[0]
    for y in range(ma[1] - mi[1] + 1):
        y += mi[1]
        p = (x, y)
        infinate = False
        if p in points:
            data[p] = [points.index(p)]
        else:
            md = min(abs(p[0] - point[0]) + abs(p[1] - point[1]) for point in points)
            o = []
            for point in points:
                d = abs(p[0] - point[0]) + abs(p[1] - point[1])
                if d == md:
                    md = d
                    o.append(points.index(point)) ##Problem, a larger value will be added if it comes first, as md will not have changed. Dosnt matter for part 1
            data[p] = o
maa = 0
for i in range(len(points)):
    infinate = False
    for key in data.keys():
        if(len(data[key]) == 1 and data[key][0] == i and (key[0] == mi[0] or key[0] == ma[0] or key[1] == mi[1] or key[1] == ma[1])):
           infinate = True
    if not infinate:
        m = len([key for key in data.keys() if len(data[key]) == 1 and data[key][0] == i])
        if m > maa:
            maa = m

#Part 1
print(maa)

#Part 2
dist = 10000
total = 0
for x in range(mi[0], ma[0] + 1):
    for y in range(mi[1], ma[1] + 1):
        d = 0
        inregion = True
        for point in points:
            d += abs(x - point[0]) + abs(y - point[1])
            if d >= dist:
                inregion = False
                break
        if inregion:
            total += 1
print(total)



