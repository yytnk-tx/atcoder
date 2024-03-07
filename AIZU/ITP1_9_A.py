W = input()

count = 0
while True:
    T = list(input().split())

    if T[0] == 'END_OF_TEXT':
        break

    for t in T:
        if t.lower() == W.lower():
            count += 1

print(count)
