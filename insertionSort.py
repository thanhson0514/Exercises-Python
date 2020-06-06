a = [9,6,3,5,8,2,4,1,7]

def insertionSort(a: list):
    for i in range(1,len(a)):
        x = a[i]
        j = i - 1

        while (a[j] > x) and j >= 0:
            a[j + 1] = a[j]
            j -= 1
        
        a[j+1] = x

insertionSort(a)
print(a)