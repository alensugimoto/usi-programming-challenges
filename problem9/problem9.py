num_questions = int(input())
answers = []
for _ in range(num_questions):
    integers = [int(strint) for strint in input().split()]
    a = integers[0]
    b = integers[1]
    x = integers[2]
    # way to ceil and floor without math module in the next two lines
    # was taken from https://stackoverflow.com/a/32559082
    min = x - 9 * ((x - a) // 9)
    max = x + 9 * ((b - x) // 9)
    min_found = False
    i = min
    while not min_found and i <= max:
        if x == sum([int(d) for d in str(i)]):
            min_found = True
            min = i
            max_found = False
            i = max
            while not max_found and i >= min:
                if x == sum([int(d) for d in str(i)]):
                    max_found = True
                    max = i
                i -= 9
        i += 9
    if min_found:
        answers.append(str(min) + " " + str(max))
    else:
        answers.append("none")
for ans in answers:
    print(ans)
