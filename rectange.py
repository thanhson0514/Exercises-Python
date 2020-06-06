class Rectange:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def perimeter(self):
        return (self.h + self.w)*2

    def acreage(self):
        return self.h*self.w

    def infor(self):
        print('height:', self.h)
        print('width:', self.w)

class SortRectange(Rectange):
    def __init__(self, h, w):
        super().__init__(h,w)

    def __lt__(self, other):
        print('test 1:',other.h, other.w,other.acreage())
        print('test 2:',self.h, self.w,self.acreage())
        if self.acreage() < other.acreage():
            return True
        elif self.acreage() == other.acreage() and self.perimeter() < other.perimeter():
            return True
     
n = int(input('Input number rectange:'))
List = []
j = 0

for i in range(n):
    print('Rectange', i+1,':')
    height = int(input('Height:'))
    width = int(input('Width:'))
    List.append(SortRectange(height, width))

List.sort()
print('Rectange after sorted:')
for i in List:
    print(f'* Rectange {j+1}:')
    i.infor()
    j += 1
