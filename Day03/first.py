n = input('Enter the target number: ')

inc = 1
cur = 1
direction = 1
h = 0
v = 0

while (inc > 0):
    for i in range(0,inc):
        if (n != cur):
            cur += 1
            h += direction
        else:
            inc = -1
            break

    if (inc < 0):
        break;

    for i in range(0, inc):
        if (n != cur):
            cur += 1
            v += direction
        else:
            inc = -1
            break

    direction *= -1
    inc += 1

print abs(h) + abs(v)
