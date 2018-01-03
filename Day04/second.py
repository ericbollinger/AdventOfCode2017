numValid = 0;

with open('input.txt') as f:
    lines = f.readlines()
    for l in lines:
        words = l.split()
        toSet = set(words)
        if (len(words) != len(toSet)):
            continue
        

        letters = []
        for w in words:
            letters.append(sorted(list(w)))

        dupe = False
        for i in range(0, len(letters)):
            for j in range(i+1, len(letters)):
                if (letters[i] == letters[j]):
                    dupe = True

        if dupe == False:
            numValid += 1

print numValid
