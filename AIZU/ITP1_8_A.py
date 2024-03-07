message = input()

for s in message:
    if s.isupper():
        print(s.lower(), end='')
    elif s.islower():
        print(s.upper(), end='')
    else:
        print(s, end='')
print()
