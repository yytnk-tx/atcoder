while True:
    m, f, r = map(int, input().split())

    if m == -1 and f == -1 and r == -1:
        break
    elif m == -1 or f == -1:
        print('F')
    elif m + f >= 80:
        print('A')
    elif 65 <= m + f < 80:
        print('B')
    elif 50 <= m + f < 65:
        print('C')
    elif (30 <= m + f < 50) and 50 <= r:
        print('C')
    elif (30 <= m + f < 50) and 50 > r:
        print('D')
    elif m + f < 30:
        print('F')
