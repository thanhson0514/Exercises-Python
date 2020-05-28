n = 4
x = [0 for i in range(n)]
def binary(i):
    for t in range(2):
        x[i] = t
        if i == n-1:
            print(x)
        else:
            print('Here')
            binary(i+1)

binary(0)