n = int(input('Nhap n:'))

max_num = min_num = n%10
temp_num = n

while temp_num > 0:
    temp = temp_num % 10
    
    if temp > max_num:
        max_num = temp
    
    temp_num //= 10

temp_num = n

while temp_num > 0:
    temp = temp_num % 10
    
    if temp < min_num:
        min_num = temp
    
    temp_num //= 10

print('So lon nhat trong', n, 'la:', max_num)
print('So be nhat trong', n, 'la:', min_num)