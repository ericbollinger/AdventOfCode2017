rows = {} 
groups = 0

with open('input.txt') as f:
    lines = f.readlines()

    # Initialize the array of connections
    i = 0
    for l in lines:
        separated = l.split(" <-> ")[1].strip()
        rows[i] = [int(x) for x in separated.split(", ")]
        i += 1

    # For as long as there are connections left in the array...
    while rows:
        resolved = []
        current = []

        # Start with "first" row remaining
        current.append(list(rows.keys())[0])

        # For as long as there are numbers left to investigate...
        while current:

            # Pop the first number, and retrieve its connection points
            n = current.pop(0)
            potential = rows[n]

            # Resolve n, if it hasn't been already (bug fix)
            if n not in resolved:
                resolved.append(n)

            # If the connection points haven't already been found, investigate them
            for r in potential:
                if r not in resolved and r not in current and r != n:
                    current.append(r)

            # Remove row from list, it's been proven to be part of a group
            rows.pop(n)
        
        # One more group down, bring on the next!
        groups += 1

    print groups
