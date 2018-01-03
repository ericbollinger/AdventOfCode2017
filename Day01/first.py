with open('input.txt') as f:
    line = list(f.readline().strip())
    nums = [int(x) for x in line]

    sum = 0

    for i in range(0, len(nums)):
        if (nums[i] == nums[(i + 1) % len(nums)]):
            sum += nums[i]

    print sum
