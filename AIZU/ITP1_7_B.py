def check(n, x, sum, count, depth):
    if sum == x and depth == 3:
        count += 1
    elif n > 0:
        for j in reversed(range(1, n)):
            if sum > x or depth == 3:
                break
            count = check(j, x, sum + j, count, depth + 1)

    return count

while True:
    n, x = map(int, input().split())

    if n == 0 and x == 0:
        break

    count = 0
    for i in reversed(range(1, n+1)):
        count = check(i, x, i, count, 1)

    print(count)
