# List = [1,2,-19,3,4,-1]
# k = int(input('Nhap k:'))

# if k > len(List):
#     print('k khong thoa man.')
# else:
#     listSum = []
#     length = len(List)-k + 1
#     for i in range(0, length):
#         Sum = 0
#         Sum += int(List[i])

#         for j in range(1,k):
#             Sum += int(List[i+j])
        
#         listSum.append(Sum)

#     print(max(listSum))

### Cach 2:
n = int(input('Nhap so phan tu:'))
k = int(input('Nhap k:'))

List = []

for i in range(n):
    x = int(input(f'Nhap phan thu thu {i+1}: '))
    List.append(x)

Sum = 0

for i in range(k):
    Sum += List[i]

result = Sum

for i in range(n-k):
    Sum += List[i+k] - List[i]

    if Sum > result:
        result = Sum

print(result)