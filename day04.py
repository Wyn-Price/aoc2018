from datetime import datetime

ma = {entry.split("[")[1].split("]")[0]: entry.split("] ")[1] for entry in open("day04input.txt", "r").read().splitlines()}

guardtimes = {}
guardminutetimes = {}

currentsleep = 0
currentguard = ""

falltime = None

def addGuardTimes(guard, minute):
    if guard in guardtimes:
        guardtimes[guard] = guardtimes[guard] + minute
    else:
        guardtimes[guard] = minute


for key in sorted(ma):
    entry = ma[key]
    if entry.startswith("Guard"):
        if currentguard != "":
            addGuardTimes(currentguard, currentsleep)
        currentguard = entry.split("#")[1].split(" ")[0]
        currentsleep = 0
    elif entry.startswith("falls"):
        falltime = datetime.strptime(key, "%Y-%m-%d %H:%M")
    elif entry.startswith("wakes"):
        cur = datetime.strptime(key, "%Y-%m-%d %H:%M")
        slm =  (cur - falltime).seconds // 60 ##It'll all be .0 anyway
        currentsleep += slm
        if currentguard not in guardminutetimes:
            guardminutetimes[currentguard] = []
        for i in range(slm):
            minute = falltime.minute + i
            guardminutetimes[currentguard].append(minute)

addGuardTimes(currentguard, currentsleep)
guard = list(entry for entry in guardtimes if guardtimes[entry] == max(guardtimes.values()))[0]
guardmins = guardminutetimes[guard]
#Part 1
print(int(guard) * max(set(guardmins), key=guardmins.count))

#Part 2
minsguard = {}
for guard in guardminutetimes:
    total = max(set(guardminutetimes[guard]), key=guardminutetimes[guard].count)
    minsguard[guardminutetimes[guard].count(total)] = (guard, total)
maxguard = minsguard[max(minsguard)]
print(int(maxguard[0]) * maxguard[1])
