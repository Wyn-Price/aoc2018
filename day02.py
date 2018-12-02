data = open("day02input.txt").read().split()

#Part 1
print(sum(1 for line in data if len(set(c for c in line if line.count(c) == 2)) != 0) * sum(1 for line in data if len(set(c for c in line if line.count(c) == 3)) != 0))

out = list(line for line in data if len(set(ol for ol in data if line != ol and sum([line[i] != ol[i] for i in range(len(line))]) == 1)) != 0)
print("".join(list(out[0][c] for c in range(0, len(out[0])) if out[0][c] == out[1][c])))