def reversePortion(arr, start, end):
    if (end < len(arr)):
        #$print "Before: " + repr(arr)
        swap = list(reversed(arr[start:end]))
        #print "Flipped: " + repr(swap)
        out = arr[0:start] + swap + arr[end:len(arr)]
        #print "After: " + repr(out) + "\n"
        return out
    else:
        #print "Before: " + repr(arr)
        tmp = []
        for i in range(start,end):
            tmp.append(arr[i%len(arr)])
        tmp = list(reversed(tmp))
        #print "Flipped: " + repr(tmp)
        split = len(arr) - start
        out = tmp[split:len(tmp)] + arr[(end%len(arr)):start] + tmp[0:split]
        #print "After: " + repr(out) + "\n"
        return out

with open('input.txt') as f:
    line = f.readline().strip()
    data = line.split(",")
    data = [int(x) for x in data]

    nums = range(0,256)
    skip = 0
    cur = 0
    for n in data:
        #print "Cur: " + repr(cur) + ", Length: " + repr(n) + ", Skip: " + repr(skip)
        nums = reversePortion(nums,cur,cur+n)
        cur = (cur + n + skip) % len(nums)
        skip += 1
        #print nums

    print nums[0] * nums[1]
