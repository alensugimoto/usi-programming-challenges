num_questions = int(input())
answers = []
for _ in range(num_questions):
    integers = input().split()
    a = integers[0]
    b = integers[1]
    x = integers[2]
    minFound = False
    while not minFound and int(b) >= int(a):
        if int(x) == sum([int(digit) for digit in a]):
            minFound = True
            maxFound = False
            while not maxFound and int(b) > int(a):
                if int(x) == sum([int(digit) for digit in b]):
                    maxFound = True
                else:
                    b = str(int(b) - 1)
        else:
            a = str(int(a) + 1)
    if minFound:
        answers.append(a + " " + b)
    else:
        answers.append("none")
for ans in answers:
    print(ans)
