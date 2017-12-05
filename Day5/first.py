with open('input.txt') as f:
    lines = f.readlines()
    jumps = [int(l.strip()) for l in lines]

    numSteps = 0
    cur = 0

    while (cur >= 0 and cur < len(jumps)):
        numSteps += 1
        newPos = jumps[cur]
        jumps[cur] += 1
        cur += newPos

    print numSteps

