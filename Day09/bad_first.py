import time
import sys

score = 0
cur = 0

def garbage():
    global score
    global cur
    while(cur < len(data)):
        if (data[cur] == '!'):
            cur += 2
        elif (data[cur] == '<'):
            cur += 1
            garbage()
        elif (data[cur] == '>'):
            cur += 1
            return
        else:
            cur += 1

def group(level):
    global score
    global cur
    score += level
    while(cur < len(data)):
        if (data[cur] == '!'):
            cur += 2
        elif (data[cur] == '{'):
            cur += 1
            group(level+1)
        elif (data[cur] == '<'):
            cur += 1
            garbage()
        elif (data[cur] == '}'):
            cur += 1
            return
        else:
            cur += 1

with open('input.txt') as f:
    sys.setrecursionlimit(1500)
    line = f.readline().strip()
    data = list(line)

    group(0)
    print score
