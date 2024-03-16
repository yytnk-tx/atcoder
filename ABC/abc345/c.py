S = input()
c = int((len(S) * (len(S)-1)) / 2)
d = 0

moji = [chr(ord('a')+i) for i in range(26)]

for i in moji:
    count = S.count(i)
    if count > 1:
        d += int((count * (count-1)) / 2)

if d == 0:
    print(c)
else:
    print(c - d + 1)
