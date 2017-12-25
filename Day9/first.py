import time

with open('input.txt') as f:
    line = f.readline().strip()
    data = list(line)

    score = 0
    depth = 0
    stack = []

    skip = False

    for i in range(0,len(data)):
        if (skip):
            skip = False
            #print "Skipping item " + repr(i)
            continue

        #time.sleep(1)
        #print repr(i) + " - " + repr(data[i]) + " - depth = " + repr(depth) + ", score = " + repr(score) + ", stack = " + repr(stack)
        if (data[i] == '!'):
            skip = True
        elif (len(stack) > 0 and stack[len(stack)-1] == '+'):
            if (data[i] == '}'):
                stack.pop()
                score += depth
                depth -= 1
            elif (data[i] == '{'):
                depth += 1
                stack.append('+')
            elif (data[i] == '<'):
                stack.append('-')

        elif (len(stack) > 0 and stack[len(stack)-1] == '-'):
            if (data[i] == '>'):
                stack.pop()

        elif (data[i] == '{'):
            depth += 1
            stack.append('+')
        elif (data[i] == '<'):
            stack.append('-')

    print score
