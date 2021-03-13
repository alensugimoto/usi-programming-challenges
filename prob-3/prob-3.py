import math

input_n = int(input())
while input_n > 0:
    print('{ ', end='')
    n = input_n - 1
    s = ''
    while n > 0:
        pow_2 = 2 ** int(math.log(n) / math.log(2))
        right = 3 ** int(math.log(pow_2) / math.log(2))
        if n == input_n - 1:
            s = str(right) + ' ' + s
        else:
            s = str(right) + ', ' + s
        n -= pow_2
    print(s + '}')
    input_n = int(input())
