class Render:
    def __init__(self, n):
        self.value = 1
        self.n = n

    def factorial(self, n):
        fac = 1
        for i in range(2,n+1):
            fac *= i
        return fac

    def run(self):
        return  self.factorial(self.n)

print(Render(8).run())