def reversePortion(arr, start, end):
    if (end < len(arr)):
        # Reverse sub-array in middle of array
        swap = list(reversed(arr[start:end]))
        return arr[0:start] + swap + arr[end:len(arr)]
    else:
        # Reverse sub-array that wraps around the end/start of array
        tmp = []
        for i in range(start,end):
            tmp.append(arr[i%len(arr)])
        tmp = list(reversed(tmp))
        split = len(arr) - start
        return tmp[split:len(tmp)] + arr[(end%len(arr)):start] + tmp[0:split]

def knotHash(string):
    # Convert input string to ASCII; append fixed sequence
    lengths = list(string)
    lengths = [int(ord(x)) for x in lengths]
    lengths += [17, 31, 73, 47, 23]

    #Run 64 rounds of KnotHash, maintaining cur and skip
    nums = range(0,256)
    cur = skip = 0
    for i in range(0,64):
        for n in lengths:
            nums = reversePortion(nums, cur, cur + n)
            cur = (cur + n + skip) % len(nums)
            skip += 1
    
    # XOR each consecutive 16 integers, resulting in 16 xor-ints
    # Then append those xor-ints together, formatted in hex
    result = ""
    for i in range(0,16):
        x = 0
        for j in range(0,16):
            x ^= nums[(i * 16) + j]
        result += '{:02x}'.format(x)

    return result

with open('input.txt') as f:
    line = f.readline().strip()
    print knotHash(line)
