def selectionSort(a: list, n: int):
    for i in range(n):
        for j in range(i,n):
            if a[j] < a[i]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    
    return a
a = [3,4,7,6,8,1,5,2]
print(selectionSort(a, len(a)))