def bubbleSort(a: list, n: int):
    for i in range(1,n):
        j = n - 1
        while j >= i:
            if a[j] < a[j-1]:
                temp = a[j-1]
                a[j - 1] = a[j]
                a[j] = temp

            j -= 1

    return a

# improved to Bubble Sort
def ShakeSort(a: list, n: int):
    left, right, k = 1,n-1,0

    while left <= right:
        j = right
        while j >= left:
            if a[j-1] > a[j]:
                temp = a[j-1]
                a[j - 1] = a[j]
                a[j] = temp
                k = j

            j -= 1
        
        left = k + 1
        j = left
        while j <= right:
            if a[j-1] > a[j]:
                temp = a[j-1]
                a[j - 1] = a[j]
                a[j] = temp
                k = j

            j += 1

        right = k - 1

    return a

a = [3,4,7,6,8,1,5,2]
b = [3,4,7,6,8,1,5,2]
print('Bubble Sort:', bubbleSort(a, len(a)))
print('Shake Sort:', ShakeSort(b, len(a)))