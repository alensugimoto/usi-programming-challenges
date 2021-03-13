import math


def rec(n):
    def rec_acc(n, P):
        if n == 0:
            return P
        else:
            pow_2 = 2 ** int(math.log(n) / math.log(2))
            left = 3 ** int(math.log(pow_2) / math.log(2))
            return rec_acc(n - pow_2, [left] + P)
    return rec_acc(n, [])


n = int(input())
while n > 0:
    if n == 1:
        print('{ }')
    else:
        print('{ %s }' % ', '.join(map(str, rec(n - 1))))
    n = int(input())
