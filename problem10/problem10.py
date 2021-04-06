n, k = [int(num) for num in input().split()]
bases = [int(base) for base in input().split()]
q = int(input())

for _ in range(q):
    l, r = [int(bound) for bound in input().split()]
    count = 0
    for i in range(n):
        for j in range(k):
            if l <= i * bases[j] <= r:
                count += 1
    print(count)
