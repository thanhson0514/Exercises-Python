print('Nhap chuoi co dang: A=B. ex: 120=111')
s = input('Input:')

index = s.find('=')

A = s[:index]
B = s[index+1:]

n = len(A)
m = len(B)
count = 0

for i in range(1, n):
    for j in range(1, m):
        aL = A[:i]
        aR = A[i:]
        bL = B[:j]
        bR = B[j:]

        if int(aL) + int(aR) == int(bL) + int(bR):
            count += 1
            print(aL, '+', aR, '=', bL, '+', bR)

if count == 0:
    print('Khong co cach dat.')
