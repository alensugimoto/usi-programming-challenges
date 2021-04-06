n, len_bases = [int(num) for num in input().split()]
bases = input().split()
num_queries = int(input())

for _ in range(num_queries):
    l, r = [int(bound) for bound in input().split()]
    count = 0
    for i in range(len_bases):
        count += r // int(bases[i]) - (l - 1) // int(bases[i])
    print(count)
