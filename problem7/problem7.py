b, c, d, l = [int(strint) for strint in input().split()]
t = 0
u = 0
num = l
v = num // d
answers = []

while v >= 0:
    while v >= 0:
        if num % d == 0:
            answers.append("%i %i %i" % (t, u, v))
        u += 1
        num = l - t * b - u * c
        v = num // d
    t += 1
    u = 0
    num = l - t * b - u * c
    v = num // d

if len(answers) == 0:
    print("impossible")
else:
    for ans in answers:
        print(ans)
