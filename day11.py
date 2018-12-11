serialnumber = 7139
data = {(x, y): 0 for x in range(301) for y in range(301)}
for x in range(1, 300):
    rackid = x + 10
    for y in range(1, 300):
        powerlevel = (rackid * y + serialnumber) * rackid
        if powerlevel < 100:
            hnum = 0
        else:
            hnum = int(str(powerlevel)[-3]) 
        data[(x, y)] = hnum - 5 + data[(x, y-1)] + data[(x-1,y)] - data[(x-1, y-1)]

def getTopLeft(size):
    ma = -999999
    out = ()
    for x in range(size, 300):
        for y in range(size, 300):
            test = data[(x, y)] - data[(x, y-size)] - data[(x-size, y)] + data[(x-size, y-size)]
            if test >= ma:
                ma = test
                out = (x - size + 1, y - size + 1, test)
    return out

tl = getTopLeft(3)
print(str(tl[0]) + "," + str(tl[1]))
maximum = 0
outsize = ()
for size in range(1, 300):
    test = getTopLeft(size)
    if test[2] > maximum:
        maximum = test[2]
        outsize = (test[0], test[1], size)

print(str(outsize[0]) + "," + str(outsize[1]) + "," + str(outsize[2]))
