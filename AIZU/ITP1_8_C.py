alpha = {}
for i in range(97, 123):
    alpha[chr(i)] = 0

Input = []
while True:
    try:
        Input.append(input())
    except EOFError:
        break

for line in Input:
    for s in line.lower():
        if s in alpha:
            alpha[s] += 1

for key, item in alpha.items():
    print(key + ' : ' + str(item))
