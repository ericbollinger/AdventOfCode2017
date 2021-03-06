import math

def findWayBack(x,y):
    cur = 0
    while (x != 0 or y != 0):
        if (x == y):
            return cur + x / 0.5
        if (x == 0):
            return cur + math.fabs(x - y)
        if (y == 0):
            return cur + (math.fabs(x - y) * 2)
        if (x > 0 and y > 0):
            x -= 0.5
            y -= 0.5
            cur += 1
        elif (x > 0 and y < 0):
            x -= 0.5
            y += 0.5
            cur += 1
        elif (x < 0 and y > 0):
            x += 0.5
            y -= 0.5
            cur += 1
        elif (x < 0 and y < 0):
            x += 0.5
            y += 0.5
            cur += 1
    return cur

steps = []

with open('input.txt') as f:
    steps = f.readline().strip()
    steps = steps.split(",")

x = 0
y = 0

for s in steps:
    if (s == "n"):
        y += 1
    elif (s == "ne"):
        y += 0.5
        x += 0.5
    elif (s == "se"):
        y -= 0.5
        x += 0.5
    elif (s == "s"):
        y -= 1
    elif (s == "sw"):
        y -= 0.5
        x -= 0.5
    elif (s == "nw"):
        y += 0.5
        x -= 0.5

print "x: " + repr(x)
print "y: " + repr(y)

answer = findWayBack(x,y)
print int(answer)
