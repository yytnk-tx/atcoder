n = int(input())
a_point, b_point = 0, 0

for _ in range(n):
    a_card, b_card = list(input().split())

    flag = False
    for a_char, b_char in zip(a_card, b_card):
        if a_char > b_char:
            a_point += 3
            flag = True
            break
        elif a_char < b_char:
            b_point += 3
            flag = True
            break
        else:
            continue
        
    if not flag:
        if len(a_card) > len(b_card):
            a_point += 3
        elif len(a_card) < len(b_card):
            b_point += 3
        else:
            a_point += 1
            b_point += 1

print(a_point, b_point)
