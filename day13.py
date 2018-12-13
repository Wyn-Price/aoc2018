dataraw = open("day13input.txt").read().splitlines()
class Cart:
    def __init__(self, x, y, direction, index):
        self.x = x
        self.y = y
        self.direction = direction
        self.index = index
        self.turndir = 0

    def move(self):
        if self.direction == 0:
            n = (0,-1)
        elif self.direction == 1:
            n = (-1,0)
        elif self.direction == 2:
            n = (0,1)
        elif self.direction == 3:
            n = (1,0)
        nex = (self.x + n[0], self.y + n[1])
        nextdata = data[nex]

        if nextdata == True:
            if self.turndir == 0:
                self.direction+=1
            elif self.turndir == 2:
                self.direction-=1
            self.direction %= 4
            self.turndir = (self.turndir + 1) % 3
        else:
            pos = (self.x, self.y)
            found = False
            for nexmove in nextdata:
                if nexmove[0] == pos:
                    self.direction = nexmove[3]
                    found = True
                    break
                elif nexmove[1] == pos:
                    found = True
                    self.direction = nexmove[2]
            if not found:
                raise Exception("Illegal Movenent")
        self.x = nex[0]
        self.y = nex[1]

def parseTrack(c, x, y):
    if c == "|":
        return [((x, y - 1), (x, y + 1), 0, 2)]
    if c == "-":
        return [((x + 1, y), (x - 1, y), 3, 1)]
    if c == "/":
        return [((x + 1, y), (x, y + 1), 3, 2), ((x - 1, y), (x, y - 1), 1, 0)]
    if c == "\\":
        return [((x, y - 1), (x + 1, y), 0, 3), ((x, y + 1), (x - 1, y), 2, 1)]
    if c == "+":
        return True
    if c.strip() == "":
        return None

    if c == "^":
        d = 0
    elif c == "<":
        d = 1
    elif c == "v":
        d = 2
    elif c == ">":
        d = 3
    else:
        raise Exception("Unknown input " + c)
    cart = Cart(x, y, d, len(carts))
    carts.append(cart)
    if d in (0, 2): #The up directions
        return parseTrack("|", x, y)
    else:
        return parseTrack("-", x, y)
carts = []
data = {(x, y): parseTrack(dataraw[y][x], x, y) for y in range(len(dataraw)) for x in range(len(dataraw[0]))}
while len(carts) > 1:
    carts.sort(key=lambda c: (c.x, c.y))
    crashedcarts = []
    for cart in carts:
        cart.move()
        pos = (cart.x, cart.y)
        for c in carts:
            if c != cart and pos == (c.x, c.y):
                print("Crash between #" + str(cart.index) + " and #" + str(c.index) + " @ " + str(c.x) + "," + str(c.y))
                crashedcarts.append(cart)
                crashedcarts.append(c)
                break
        if len(carts) - len(crashedcarts) == 1:
            break
    for cart in crashedcarts:
        carts.remove(cart)
cart = carts[0]
print("Cart #" + str(cart.index) + " finishes at position " + str(cart.x) + "," + str(cart.y))



