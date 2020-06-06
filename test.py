def hangmanGame(text, answers):
    for st in text:
        if st not in answers:
            return False
    
    return True

# print(hangmanGame("code",["c", "d","y", "i", "e", "o", "n"]))

def miniMaxSum(arr):
    total = []

    # big-O(n)
    for i in range(len(arr)): # n
        c = arr[:i] + arr[i+1:] # 1
        print(c) # 1
        s = sum(c) # 1
        total.append(s) # 1
        # 4*n => n
    
    print(min(total), max(total))

# print(miniMaxSum([1,2,3,4,5]))

def printPicture():
    n = int(input('Nhap n'))

    for i in range(n):
        print(' '*(n-i), end='')
        if i == 0: print('*')
        else: 
            print('*', end='')
            print(' '*(2*i-1), end='')
            print('*')

    for i in range(n-1):
        print(' '*(i+2), end='')
        if i == n-2: print('*')
        else:
            print('*',end='')
            print(' '*(2*(n-i-2)-1),end='')
            print('*')

def f(k):
    return 2*k - 1

def cal_number(k):
    total = 0
    for i in range(1,k+1):
        total += f(i)
        print(f(i))

    return i

cal_number(2)
