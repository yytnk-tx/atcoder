def CHECK_NUM(x):
    if x % 3 == 0:
        return True
    else:
        return False

def INCLUDE3(x):
    if x % 10 == 3:
        return True
    else:
        if x // 10:
            return INCLUDE3(x // 10)
        else:
            return False

n = int(input())

for i in range(1, n+1):
    x = i
    if CHECK_NUM(x):
        print(' ' + str(i), end='')
        continue
    if INCLUDE3(x):
        print(' ' + str(i), end='')
print()
