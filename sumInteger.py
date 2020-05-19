# c != 0, if c > 0 then a < b, else if c < 0 a > b
# c call same is step

n = int(input('Nhap n:'))

Sum = 0

while n > 0:
    temp = n%10
    Sum += temp
    n //= 10

print('Tong cac chu so la:', Sum)

