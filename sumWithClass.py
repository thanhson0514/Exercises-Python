'''
    - Calculator sum a list
    - Calculator min element
    - Calculator max element
    - Find couple element have sum is 0
'''

class List:
    def __init__(self, arr):
        self.arr = arr

    def sumList(self):
        return sum(self.arr)
    
    def minList(self):
        return min(self.arr)
   
    def maxList(self):
        return max(self.arr)

    def coupleSumZero(self):
        storeZero = []
        for i in range(len(self.arr)-1):
            for j in range(i+1, len(self.arr)):
                if self.arr[i] + self.arr[j] == 0: storeZero.append((self.arr[i], self.arr[j]))

        return storeZero

n = List([1,2,-1,0,-2,3])
print(n.coupleSumZero())