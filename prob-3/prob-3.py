import math


def rec(n, is_first):
    if n != 0:
        pow_2 = 2 ** int(math.log(n) / math.log(2))
        right = 3 ** int(math.log(pow_2) / math.log(2))
        rec(n - pow_2, False)
        print(right, end='')
        if not is_first:
            print(',', end='')
        print(' ', end='')


n = int(input())
while n > 0:
    print('{ ', end='')
    rec(n - 1, True)
    print('}')
    n = int(input())
