import time

with open('input.txt') as f:
    line = f.readline().strip().split()
    banks = [int(x) for x in line]

banks_seen = []
num_banks = len(banks)
run = 1

banks_seen.append(list(banks))

while(run > 0):
    toDistribute = max(banks)
    fromHere = banks.index(toDistribute)
    banks[fromHere] = 0
    for i in range(1, toDistribute + 1):
        banks[(fromHere + i) % num_banks] += 1

    for seen in banks_seen:
        if (seen == banks):
            print run - banks_seen.index(seen)
            run = -2

    banks_seen.append(list(banks))
    run += 1
