def find_min(a, b, x):
    zeros = 0
    while True:
        min = str(int(x) % 9) + zeros * "0" + (int(x) // 9) * "9"
        zeros += 1
        if int(min) > int(b):
            return "none"
        elif int(min) >= int(a):
            return min


num_questions = int(input())
for _ in range(num_questions):
    a, b, x = [int(strint) for strint in input().split()]
    min = find_min(a, b, x)
    if min == "none":
        print("none")
        continue
    min = int(min)
    max = int(x) + 9 * ((int(b) - int(x)) // 9)
    while max > min:
        if int(x) == sum([int(d) for d in str(max)]):
            break
        max -= 9
    print("%i %i" % (min, max))
