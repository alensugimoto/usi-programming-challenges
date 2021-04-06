n, len_bases = [int(num) for num in input().split()]
bases = [int(base) for base in input().split()]
num_queries = int(input())

for _ in range(num_queries):
    l, r = [int(bound) for bound in input().split()]
    count = 0
    for i in range(len_bases):
        count += r // bases[i] - (l - 1) // bases[i]
    print(count)
