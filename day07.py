lettersc = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
datac = {}
for line in open("day07input.txt", "r").read().splitlines():
    let = line.split()[7]
    if let not in datac:
        datac[let] = []
    datac[let].append(line.split()[1])
data = {key: datac[key][:] for key in datac.keys()}

letters = lettersc[:]

#Part 1
out = ""
while letters:
    cand = [l for l in letters if l not in data or len(data[l]) == 0]
    cand.sort()
    le = cand[0]
    out += le
    letters.remove(le)
    for value in data.values():
        if le in value:
            value.remove(le)
print(out)

data = datac
letters = lettersc[:]

#Part 2
time = 0
totworkers = 5
workers = [[0, ""] for i in range(totworkers)]
while letters or any(worker[0] > 0 for worker in workers):
    cand = [l for l in letters if l not in data or len(data[l]) == 0]
    cand.sort()
    for w in workers:
        w[0] -= 1
        if w[0] <= 0:
            for value in data.values():
                if w[1] in value:
                    value.remove(w[1])
            if cand:
                le = cand.pop(0)
                w[0] = 60 + lettersc.index(le)
                w[1] = le
                letters.remove(le)
    time += 1

print(time)








