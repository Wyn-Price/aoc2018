data = [int(c) for c in open("day08input.txt", "r").read().split()]
pointer = 0

class Node:
    def __init__(self):
        global pointer
        global data

        self.children = []
        self.metadata = []

        cs = data[pointer]
        pointer += 1
        ms = data[pointer]
        pointer += 1
        for i in range(cs):
            self.children.append(Node())
        for i in range(ms):
            self.metadata.append(data[pointer])
            pointer += 1


    def getMeta(self):
        return sum(m for m in self.metadata) + sum(c.getMeta() for c in self.children)

    def getValue(self):
        if len(self.children) == 0:
            return self.getMeta()
        out = 0
        for m in self.metadata:
            m -= 1
            if m >= 0 and m < len(self.children):
                out += self.children[m].getValue()
        return out

root = Node()
print(root.getMeta())
print(root.getValue())



