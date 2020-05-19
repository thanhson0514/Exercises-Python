n = int(input('Nhap so nguyen duong N:'))

primes = [True]*n

primes[0] = False
primes[1] = False
store = []

for i in range(2,len(primes)):
    if primes[i]:
        store.append(i)
        for j in range(i*i,len(primes), i):
            primes[j] = False

for i in store:
    print(i)

