import math

input_n = int(input())
while input_n > 0:
    print('{ ', end='')
    n = input_n - 1
    s = ''
    while n > 0:
        # convert 'n' to the greatest power of 2 less than or equal to it
        bits = bin(n)
        pow_2 = int(bits[:3] + '0' * (len(bits) - 3), 2)
        # find the log base 2 of 'pow_2'
        log_pow_2 = len(bin(pow_2)) - 3
        # get rightmost element
        right = 3 ** log_pow_2
        # store in 's'
        if n == input_n - 1:
            s = str(right) + ' ' + s
        else:
            s = str(right) + ', ' + s
        # prepare for next iteration
        n -= pow_2
    print(s + '}')
    input_n = int(input())
