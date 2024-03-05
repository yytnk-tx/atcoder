N, M, L = map(int, input().split())
A, B, C = [], [], []

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(M):
    B.append(list(map(int, input().split())))

for n in range(N):
    C.append([])
    for l in range(L):
        sum = 0
        for m in range(M):
            sum += A[n][m] * B[m][l]
        C[n].append(str(sum))
    print(' '.join(C[n]))
