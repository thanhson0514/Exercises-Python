n = int(input('Nhap n:'))
print('Nhap',n, 'so:')
list1 = [int(input()) for i in range(n)]
print('Nhap', n, 'ten:')
list2 = [input() for i in range(n)]

dictionary = {}

for i in range(len(list1)):
    dictionary[list1[i]] = list2[i]

print(dictionary)