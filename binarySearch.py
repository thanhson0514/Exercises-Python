a = [1,3,5,10,15,21,24,95,99]

def binarySearch(a: list, x: int) -> int:
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end)//2
        print(a[mid],mid)
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            start = mid + 1
        elif a[mid] > x:
            end = mid - 1

    return False 

print(binarySearch(a, 2))