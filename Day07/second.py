# This suuuuucks but it works.
# The proper solution is the first entry labeled ANSWER.

import re

def indexDifferentValue(arr):
    for i in range(0,len(arr)-1):
        if (arr[i] != arr[i+1]):
            if (i == 0):
                if (arr[i+1] != arr[i+2]):
                    return i+1
                return i
            return i+1

def checkWeights(x):
    if (len(order[x]) == 0):
        return weights[x]
    else:
        sum = 0
        each = []
        for i in order[x]:
            n = checkWeights(i)
            each.append(n)
            sum += n
        if (len(set(each)) > 1):
            #print(each)
            indexDiff = indexDifferentValue(each)
            #print "Index: " + repr(indexDiff)

            diff = each[indexDiff] - each[(indexDiff + 1) % len(each)]
            #print diff

            new = weights[order[x][indexDiff]] - diff
            #print "Orig: " + repr(weights[order[x][indexDiff]])
            print "ANSWER: " + repr(new)

            #print "\n"
            #for i in order[x]:
            #    print i + ": " + repr(weights[i])

        return weights[x] + sum


with open('input.txt') as f:
    lines = list(f.readlines())
    lines = [x.strip() for x in lines]

    nodes = []
    counted = []
    values = []
    stacked = []
    for l in lines:
        item = l.split()
        nodes.append(item[0])
        values.append(int(re.sub('[()]','',item[1])))

        ontop = []
        if (len(item) > 2):
            for i in range (3,len(item)):
                n = re.sub('[,]','',item[i])
                ontop.append(n)
                counted.append(n)
        stacked.append(ontop)

    bottom = list(set(nodes) - set(counted))[0]
    #print bottom

    weights = dict(zip(nodes, values))
    order = dict(zip(nodes, stacked))
    
    checkWeights(bottom)
