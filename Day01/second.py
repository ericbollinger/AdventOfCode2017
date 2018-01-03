with open('input.txt') as f:
    line = list(f.readline().strip())
    nums = [int(x) for x in line]

    sum = 0
    length = len(nums)
    offset = length/2

    for i in range(0, len(nums)):
        if (nums[i] == nums[(i + offset) % length]):
            sum += nums[i]

    print sum
