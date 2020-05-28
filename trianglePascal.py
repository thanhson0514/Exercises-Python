def printTriangle(L, n):
    print(' '*n, end='')

    for i in L:
        print(i, end=' ')
    print('\n')

def pascal(n):
    list1 = [1]
    d = 0
    z = n
    while d <= n:
        printTriangle(list1, z)
        list2 = [] + list1

        for i in range(len(list1) - 1):
            list1[i+1] = list2[i+1] + list2[i]

        list1 += [1]
        d += 1
        z -= 1

pascal(10)