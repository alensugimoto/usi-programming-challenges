T = int(input())
for t in range(T):
    n = int(input())
    seg = input().split()
    B, R = [], []
    for i in range(0, 2 * n, 2):
        if seg[i + 1] == "B":
            B.append(int(seg[i]))
        elif seg[i + 1] == "R":
            R.append(int(seg[i]))
    if len(B) > len(R):
        B.sort(reverse=True)
    elif len(R) > len(B):
        R.sort(reverse=True)
    max = 0
    for i in range(min(len(B), len(R))):
        max += B[i] + R[i] - 2
    print("Case #%i: %i" % (t + 1, max))
