num_names = int(input())
if num_names >= 0:
    print('Hello', end='')
    if num_names == 0:
        print(' World!')
    elif num_names == 1:
        print(' %s!' % input())
    elif num_names == 2:
        print(' %s and %s!' % (input(), input()))
    else:
        for i in range(num_names):
            name = input()
            if i == num_names - 1:
                print(' and %s!' % name)
            else:
                print(' %s,' % name, end='')
