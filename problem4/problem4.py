def next_b(b):
    new_b = str(int(b) + 1)
    length = len(new_b)
    zeros = 0
    while int(new_b[-1 - zeros]) == 0:
        zeros += 1
    return str(int(b) - int(new_b[-1 - zeros] + "0" * zeros))


def go_to_max(b, x):
    if int(x) <= int(b[0]):
        return x + "0" * (len(b) - 1)
    else:
        return b[0] + go_to_max(b[1:], str(int(x) - int(b[0])))


def find_max(a, b, x):
    if int(a) > int(b):
        return "none"
    else:
        first = int(b[0])
        length = len(b)
        summ = sum([int(digit) for digit in b])
        if summ == int(x):
            return b
        elif summ > int(x):
            return go_to_max(b, x)
        elif length == 1:
            return "none"
        else:
            return find_max(a, next_b(b), x)


def go_to_min(a, x):
    summ = sum([int(digit) for digit in a])
    nines = 0
    add = 9 - int(a[-1])
    while int(x) - summ > add:
        if len(a) < nines + 1:
            a = "9" + a
        else:
            a = a[:-1 - nines] + "9" + a[len(a) - nines:]
        summ += add
        nines += 1
        if len(a) < nines + 1:
            add = 9
        else:
            add = 9 - int(a[-1 - nines])
    return str(int(a) + (int(x) - summ) * 10 ** nines)


def find_min(a, b, x):
    if int(a) >= int(b):
        return b
    else:
        first = int(a[0])
        length = len(a)
        summ = sum([int(digit) for digit in a])
        if summ == int(x):
            return b
        elif summ < int(x):
            min = go_to_min(a, x)
            if int(min) < int(b):
                return min
            else:
                return b
        else:
            return find_min(str(10 ** length), b, x)


num_questions = int(input())
answers = []
for _ in range(num_questions):
    integers = input().split()
    a = integers[0]
    b = integers[1]
    x = integers[2]
    max = find_max(a, b, x)
    if max == "none":
        answers.append("none")
    else:
        min = find_min(a, max, x)
        answers.append(min + " " + max)
for ans in answers:
    print(ans)
