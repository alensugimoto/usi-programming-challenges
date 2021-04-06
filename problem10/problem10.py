n, len_bases = [int(num) for num in input().split()]
bases = [int(base) for base in input().split()]
num_queries = int(input())

for _ in range(num_queries):
    l, r = [int(bound) for bound in input().split()]
    count = 0
    for i in range(len_bases):
        l_mult = -(-l // bases[i]) * bases[i]
        if l_mult <= r:
            count += (r - l_mult) // bases[i] + 1
    print(count)
