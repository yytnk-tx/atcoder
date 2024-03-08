N = int(input())
A = list(map(int, input().split()))

count = 0

while True:
    is_all_even = True
    for i in range(N):
        if A[i] % 2 == 1:
            is_all_even = False
            break
    
    if is_all_even:
        A = list(map(lambda x: int(x/2), A))
        count += 1
    else:
        break

print(count)
