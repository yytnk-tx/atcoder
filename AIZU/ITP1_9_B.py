while True:
    str = input()
    if str == '-':
        break
    cards = list(str)

    m = int(input())
    for _ in range(m):
        h = int(input())
        for _ in range(h):
            cards.append(cards.pop(0))

    print(*cards, sep='')
