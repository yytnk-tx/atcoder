def search_card(l, suit, missing_cards):
    for i in range(13):
        if missing_cards == 0:
            break

        if l[i] == 1:
            continue

        print(suit, i + 1)
        missing_cards -= 1

    return missing_cards

ALL = 52
n = int(input())
missing_cards = ALL - n

s = [0 for _ in range(13)]
h = [0 for _ in range(13)]
c= [0 for _ in range(13)]
d = [0 for _ in range(13)]

for _ in range(n):
    suit, rank = input().split()
    
    if suit == 'S':
        s[int(rank) - 1] = 1
    if suit == 'H':
        h[int(rank) - 1] = 1
    if suit == 'C':
        c[int(rank) - 1] = 1
    if suit == 'D':
        d[int(rank) - 1] = 1

if missing_cards != 0:
    missing_cards = search_card(s, 'S', missing_cards)
if missing_cards != 0:
    missing_cards = search_card(h, 'H', missing_cards)
if missing_cards != 0:
    missing_cards = search_card(c, 'C', missing_cards)
if missing_cards != 0:
    missing_cards = search_card(d, 'D', missing_cards)
