w, l = [int(length) for length in input().split()]
house_num = 1
while w != 0 or l != 0:
    rows = []
    for _ in range(l):
        rows.append(input())
    enter = [0, 0]
    for row in range(l):
        for col in range(w):
            if rows[row][col] == "*":
                enter = [col, row]
    col = enter[0]
    row = enter[1]
    dir = [0, 0]
    if col == 0:
        dir = [1, 0]
    elif col == w - 1:
        dir = [-1, 0]
    elif row == 0:
        dir = [0, 1]
    else:
        dir = [0, -1]
    col += dir[0]
    row += dir[1]
    while row != 0 and row != l - 1 and col != 0 and col != w - 1:
        if rows[row][col] == "/":
            dir[0], dir[1] = -dir[1], -dir[0]
        elif rows[row][col] == "\\":
            dir[0], dir[1] = dir[1], dir[0]
        col += dir[0]
        row += dir[1]
    rows[row] = rows[row][:col] + "&" + rows[row][col + 1:]
    print("HOUSE", house_num)
    for row in rows:
        print(row)
    w, l = [int(length) for length in input().split()]
    house_num += 1
