operands = []

with open('input.txt') as f:
    lines = f.readlines()
    for l in lines:
        nums = [int(x) for x in l.split()]
        for i in range (0, len(nums)):
            for j in range (0, len(nums)):
                if (i != j and nums[j] % nums[i] == 0):
                    operands.append(nums[j] / nums[i])
                    i = len(nums)-1
                    j = len(nums)-1

sum = 0
for n in operands:
    sum += n

print sum
