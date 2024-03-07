while True:
    datasets = input()

    if datasets == '0':
        break

    sum = 0
    for data in datasets:
        sum += int(data)
    
    print(sum)
