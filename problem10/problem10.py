n, k = [int(num) for num in input().split()]
bases = [int(base) for base in input().split()]
q = int(input())

for _ in range(q):
    l, r = [int(bound) for bound in input().split()]
    count = 0
    more = True
    i = 0
    while more:
        more = False
        for j in range(k):
            if l <= bases[j] * i <= r:
                count += 1
            if bases[j] * i <= r:
                more = True
        i += 1
    print(count)
