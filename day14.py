numtimes = 640441
recipes = [3, 7]
recipe10 = []

elfs = [i for i in range(2)]
timer = 0
part1 = None
part2 = None
numhits = 0
while not part1 or not part2:
    new = sum(recipes[i] for i in elfs)
    if len(recipes) < numtimes + 10:
        part1 = recipes
    for c in str(new):
        if c == str(numtimes)[numhits]:
            numhits += 1
        else:
            numhits = 0
        recipes.append(int(c))
        if numhits == len(str(numtimes)):
            part2 = len(recipes) - numhits
    for i in range(len(elfs)):
        elfs[i] = (elfs[i] + 1 + recipes[elfs[i]]) % len(recipes)

print("".join(map(str, part1[-10:])))
print(part2)
