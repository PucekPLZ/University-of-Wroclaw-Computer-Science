def tab(x1, x2, y1, y2, d):
    max_width = max(len(str(x2)), len(str(y2)), len(str(x2 * y2)))

    print(f'{"":<{max_width}}', end='\t')

    for x in range(int(x1), int(x2) + 1, int(d)):
        print(f'{float(x):<{max_width}}', end='\t')

    print() 

    for y in range(int(y1), int(y2) + 1, int(d)):
        print(f'{float(y):<{max_width}}', end='\t')

        for x in range(int(x1), int(x2) + 1, int(d)):
            result = x * y
            print(f'{float(result):<{max_width}}', end='\t')

        print()

tab(-3.0, 5.0, 2.0, 4.0, 1.0)