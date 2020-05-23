n = int(input('Nhap n:'))

list1 = [int(input()) for i in range(n)]
couple = []

for i in range(n):
    for j in range(i,n):
        x = []
        if list1[i]+1 == list1[j]:
            x.append(i+1)
            x.append(j+1)

        if len(x) != 0: couple.append(x)

print(couple)