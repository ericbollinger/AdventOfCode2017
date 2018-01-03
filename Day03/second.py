items = []

def getVal(x,y):
    if (len(items) == 0):
        return 1

    x_vals = [x-1, x, x+1]
    y_vals = [y-1, y, y+1]

    sum = 0

    for i in items:
        if i[1] in x_vals and i[2] in y_vals:
            sum += i[0]

    return sum


inc = 1
cur = 1
direction = 1
x = 0
y = 0

n = input("Enter your target number: ")

while (inc > 0):

    for i in range(0,inc):
        if (n >= cur):
            cur = getVal(x,y)
            items.append([cur,x,y])
            x += direction
        else:
            inc = -1
            break

    if (inc < 0):
        break;

    for i in range(0, inc):
        if (n >= cur):
            cur = getVal(x,y)
            items.append([cur,x,y])
            y += direction
        else:
            inc = -1
            break

    direction *= -1
    inc += 1

print cur
