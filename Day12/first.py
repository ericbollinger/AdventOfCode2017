rows = {} 

with open('input.txt') as f:
    lines = f.readlines()

    # Initialize the array of connections
    i = 0
    for l in lines:
        separated = l.split(" <-> ")[1].strip()
        rows[i] = [int(x) for x in separated.split(", ")]
        i += 1

    resolved = []
    current = [0]

    # For as long as there are numbers left to investigate, starting with 0...
    while current:

        # Pop the first number, and retrieve its connection points
        n = current.pop(0)
        potential = rows[n]

        # If the connection points haven't already been found, investigate them
        for r in potential:
            if r not in resolved and r not in current:
                current.append(r)

        # Resolve nn, if it hasn't been already (bug fix)
        if n not in resolved:
            resolved.append(n)

    print len(resolved)
