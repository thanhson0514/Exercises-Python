n = int(input('Nhap n:'))
k = int(input('Nhap k:'))

factorial = 1
string = ''

for i in range(2,n+1):
    factorial *= i
    n = factorial
    string = ''
    j = 0
    
    while j < k:
        x = n%10
        string += str(x) 
        j += 1
        n //= 10
        if n < 0: break

    factorial %= 10**k

print(string[::-1])
print(factorial)