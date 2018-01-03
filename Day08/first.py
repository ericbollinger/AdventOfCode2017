def getRegValue(x):
    if (x not in regs.keys()):
        regs[x] = 0
        return 0
    return regs[x]

def runTest(reg, op, num):
    if (op == '>'):
        return (getRegValue(reg) > num)
    elif (op == '<'):
        return (getRegValue(reg) < num)
    elif (op == '>='):
        return (getRegValue(reg) >= num)
    elif (op == '<='):
        return (getRegValue(reg) <= num)
    elif (op == '=='):
        return (getRegValue(reg) == num)
    elif (op == '!='):
        return (getRegValue(reg) != num)

with open('input.txt') as f:
    regs = {}

    lines = list(f.readlines())
    lines = [x.strip() for x in lines]

    for l in lines:
        items = l.split()
        cond = items[4]
        op = items[5]
        num = int(items[6])

        if (runTest(cond, op, num)):
            reg = getRegValue(items[0])
            if (items[1] == 'inc'):
                reg += int(items[2])
            else:
                reg -= int(items[2])
            regs[items[0]] = reg

        else:
            continue

    print max(regs.values())
