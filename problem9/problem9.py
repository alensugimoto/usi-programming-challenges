def digit_sum(n):
    count = 0
    while n > 0:
        count += n % 10
        n //= 10
    return count


def find_lower(a, b, x):
    a, b, x = int(a), int(b), int(x)
    # find lower's lower bound
    llower = a
    digit = 1
    while True:
        llower = digit * a
        llower_ds = digit_sum(llower)
        if x >= llower_ds:
            break
        digit *= 10
        a = -(-a // 10)
    # return if possible
    if b < llower:
        return "none"
    if x == llower_ds:
        return str(llower)
    if b == llower:
        return "none"
    # get lower from its lower bound
    lower = llower
    x -= llower_ds
    i = 0
    while x > 0:
        index = len(str(lower)) - 1 - i
        if index >= 0:
            n = min(x, 9 - int(str(lower)[index]))
        else:
            n = min(x, 9)
        lower += n * 10 ** i
        x -= n
        i += 1
        if b < lower:
            return "none"
    return str(lower)


def find_upper(a, b, x):
    a, b, x = int(a), int(b), int(x)
    # find upper's upper bound,
    # and if it is upper, return it
    uupper_found = False
    uupper = b
    digit = 0
    while b > 0 and not uupper_found:
        if digit == 0:
            uupper_ds = digit_sum(uupper)
            digit = 1
        else:
            uupper = digit * b - 1
            uupper_ds = digit_sum(uupper)
            digit *= 10
            b //= 10
        uupper_found = x <= uupper_ds
    # return if possible
    if not uupper_found:
        return "none"
    if x == uupper_ds:
        return str(uupper)
    if a >= uupper:
        return "none"
    # get upper from its upper bound
    upper = 0
    for i in range(len(str(uupper))):
        n = min(x, int(str(uupper)[i]))
        upper += n * 10 ** (len(str(uupper)) - 1 - i)
        x -= n
    if a > upper:
        return "none"
    return str(upper)


num_questions = int(input())
for _ in range(num_questions):
    a, b, x = [int(strint) for strint in input().split()]
    lower = find_lower(a, b, x)
    if lower == "none":
        print("none")
        continue
    upper = find_upper(lower, b, x)
    print(lower + " " + upper)
