str = list(input())
q = int(input())

for _ in range(q):
    command = list(input().split())

    if command[0] == 'print':
        print(*str[int(command[1]):int(command[2])+1], sep='')
    elif command[0] == 'reverse':
        str[int(command[1]):int(command[2])+1] = reversed(str[int(command[1]):int(command[2])+1])
    elif command[0] == 'replace':
        str[int(command[1]):int(command[2])+1] = command[3]
