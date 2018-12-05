import string

data = list(open("day05input.txt", "r").read())
#Part 1
def react(data):
    data = data[:]
    while True:
        done = True
        for i in range(len(data) - 1):
            c1 = data[i]
            c2 = data[i + 1]

            if c1.lower() == c2.lower() and c1 != c2:
                data.pop(i)
                data.pop(i)
                done =  False
                break;
        if done:
            break;
    return data

print(len(react(data)))

#Part 2
lowest = (999999, "")
for char in string.ascii_lowercase:
    filteredlen = len(react([c for c in data if c.lower() != char]))
    if filteredlen < lowest[0]:
        lowest = (filteredlen, char)
    print("Interpreted " + char)


print(lowest)

