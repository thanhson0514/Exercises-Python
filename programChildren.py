def maxValue(*x):
    return max(x)

def sum_square(x):
    l = []
    for i in x:
        l.append(i**2)
    return sum(l)

def sum_cube(x):
    l = []
    for i in x:
        l.append(i**3)
    return sum(l)

def function(f, x):
    return f(x)

print(function(sum_square,[1,2,3,4]))
print(function(sum_cube,[1,2,3,4]))
