operands = list()

with open('input.txt') as f:
    lines = f.readlines()
    for l in lines:
        nums = [int(x) for x in l.split()]
        operands.append(max(nums) - min(nums))

sum = 0;
for n in operands:
    print n
    sum = sum + n
    print sum

print sum

