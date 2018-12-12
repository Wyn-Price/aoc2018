import re, collections
raw = open("day12input.txt").read()
initialstates = re.findall(r"initial state:\s(.+)\s*", raw)[0]
current = collections.defaultdict(lambda: ".", {i:initialstates[i] for i in range(len(initialstates))})
changes = re.findall(r"([#|\.]{5})\s=>\s(#|\.)", raw)
diffs = {}
prev = 0
gens = 50000000000
for gen in range(gens):
    newstate = collections.defaultdict(lambda: ".", {i:"." for i in range(len(current))})
    for c in range(-4, len(current)+4):
        section = ""
        for i in range(c-2, c+3):
            section += current[i]
        for (test, new) in changes:
            if test == section:
                newstate[c] = new
    current = newstate
    currentsum = sum(list(i for i in current.keys() if current[i] == "#"))
    diff = currentsum - prev
    if gen == 19:
        print(currentsum)
    if diff in diffs and diffs[diff] > 200: #Total of 1000 occurnces of the same diffrence
        print(currentsum + (gens - gen - 1) * diff)
        break;
    if diff not in diffs:
        diffs[diff] = 1
    else:
        diffs[diff] += 1
    prev = currentsum
