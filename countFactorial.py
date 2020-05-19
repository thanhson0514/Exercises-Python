n = int(input('Nhap N:'))
k = int(input('Nhap k chu so cuoi:'))
factorial = 1
stores = []
string = ''

for i in range(1,n+1):
    factorial *= i

    n = factorial
    i = 1
    string = ''

    while i <= k:
        x = n%10
        string += str(x)
        n //= 10
        i += 1

        if n <= 0:
            break

    factorial %= 10**k

print(string[::-1])
print('factorial:', factorial)
