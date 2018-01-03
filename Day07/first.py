import re

with open('input.txt') as f:
    lines = list(f.readlines())
    lines = [x.strip() for x in lines]

    full = []
    found = []
    for l in lines:
        item = l.split()
        full.append(item[0])
        if (len(item) > 2):
            for i in range(3,len(item)):
                found.append(re.sub('[,]','',item[i]))

    diff = set(full) - set(found)
    print diff
