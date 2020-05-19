n = int(input('Ma tran cap:'))

List = []
print('Nhap so phan tu cua ma tran:')
for i in range(n):
    row = []
    print('Nhap dong thu', i+1, ':')
    for j in range(n):
        x = int(input())
        row.append(x)
    
    List.append(row)

sum1 = 0
sum2 = 0

for i in range(n):
    sum1 += List[i][i]

for i in range(n):
    sum2 += List[i][n-1-i]

print(sum1)
print(sum2)