'''
 ((({{}})))
'''
class Stack:
    def __init__(self):
        self.store = []

    def push(self, item):
        self.store.append(item)

    def pop(self):
        self.store.pop()

    def peek(self):
        return self.store[-1]

    def is_empty(self):
        return self.store == []

    def show(self):
        return self.store

# (
def balance_brake(string):
    s = Stack()
    for i in string:
        if i in '([{':
            s.push(i)
        else:
            if s.is_empty(): return False
            if i == ')': s.pop()
            elif i == '}': s.pop()
            elif i == ']': s.pop()
            else: return False

    if s.is_empty(): return True
    else: return False

def integer_bin(n):
    s = Stack()
    while n > 0:
        if n%2 == 0:
            t = n%2
            s.push(t)
            n //= 2
        else:
            t = n%2
            s.push(t)
            n //= 2

    return s.show()

print(int('010', 2))
print(integer_bin(2))
print(balance_brake('())(())'))