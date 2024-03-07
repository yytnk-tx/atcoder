s = input()
p = input()

flag = False

for i in range(len(s)):
    if len(p) + i > len(s):
        if s[i:len(s)] + s[0:len(p)-(len(s)-i)] == p:
            flag = True
            break
    else:
        if s[i:len(p)+i] == p:
            flag = True
            break

if flag:
    print('Yes')
else:
    print('No')
