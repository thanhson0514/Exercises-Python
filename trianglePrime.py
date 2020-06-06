t = 2
def isPrime(c): # 3 + n*(7 + t*2) => n*(t+1)
    global t
    d = 0 # 1
    temp = [] # 1
    while d <= c: # n
        prime = True # 1
        for i in range(2,t): # t
            if t%i == 0: # 1
                prime = False # 1
        
        if prime: # 1
            temp.append(t) # 1
            d += 1 # 1

        t += 1 # 1
        if d > c: # 1
            return temp # 1

def trianglePrime(n): # 1 + n*(3 + 3 + n*(7 + t*2)) => 1 + n*(9 + n*(7+2*t))
    space = n # 1
    for i in range(n): # n
        print(' '*(space), end='') # 1
        a = isPrime(i) # 3 + n*(7 + t*2)
        for i in a: # 3 + n*(7 + t*2)
            print(i, end=' ') # 1

        print() # 1

        space -= 1 # 1


n = int(input('Input N:'))

# => big-O(n^2 + t*n)
trianglePrime(n)