numValid = 0;

with open('input.txt') as f:
    lines = f.readlines()
    for l in lines:
        words = l.split()
        toSet = set(words)
        if (len(words) == len(toSet)):
            numValid += 1

print numValid
