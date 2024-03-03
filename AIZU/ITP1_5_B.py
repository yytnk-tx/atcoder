while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break

    print('#'*W)
    for _ in range(1, H-1):
        print('#', end='')
        for _ in range(1, W-1):
            print('.', end='')
        print('#')
    print('#'*W, end='\n\n')
