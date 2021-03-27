T = int(input())
for t in range(T):
    n = int(input())
    pairs = input().split()
    max = 0
    for _ in range(n // 2):
        maxB, posB = 0, 0
        maxR, posR = 0, 0
        for i in range(1, len(pairs), 2):
            length = int(pairs[i - 1])
            if pairs[i] == "B" and length > maxB:
                maxB = length
                posB = i - 1
            elif pairs[i] == "R" and length > maxR:
                maxR = length
                posR = i - 1
        if maxB == 0 or maxR == 0:
            break
        max += maxB + maxR - 2
        pairs = pairs[:posB] + pairs[posB + 2:]
        pairs = pairs[:posR] + pairs[posR + 2:]
    print("Case #%i: %i" % (t + 1, max))
