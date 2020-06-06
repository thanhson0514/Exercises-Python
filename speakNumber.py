n = int(input('Nhập số: '))

while len(str(n)) > 10:
    print('Số nguyên không được lớn hơn 9 chữ số. Mời nhập lại:')
    n = int(input())

n = str(n)
l = len(n)
copy_n = n
number = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']
speak = []
count = 0

if n == '0' and l == 1: print('không')
while n != '':
    t = n[-3:]
    if int(t) == 0:
        if l >= 4 and count == 0: speak.append('nghìn')
        elif l >= 7 and count == 1:
            temp = speak.pop()
            if temp != 'nghìn': speak.append(temp)
            speak.append('triệu')
        elif l >= 10 and count == 2:
            temp = speak.pop()
            if temp != 'triệu': speak.append(temp)
            speak.append('tỷ')
    else:
        zero = 0
        p = 0
        
        for i in range(len(t)-1,-1,-1):
            if p == 2 and l > 2: speak.append('trăm')
            speak.append(number[int(t[i])])

            if t[i] == '5' and p == 0 and l > 1: 
                    speak.pop()
                    speak.append('lăm')
            elif t[i] == '0' and p == 0:
                speak.pop()
                speak.append('mười')

                zero += 1

            if t[i] == '0' and p == 1 and l > 2 and zero != 1:
                speak.pop()
                speak.pop()
                temp = speak.pop()
                if temp == 'mốt': speak.append('một')
                else: speak.append(temp)
                speak.append('lẻ')
            elif zero == 1 and p == 1 and t[i] == '0': 
                speak.pop()
                speak.pop()
            elif t[i] != '0' and p == 0 and len(t) > 1 and zero != 1: 
                if t[i-1] != '1': 
                    temp = speak.pop()
                    if temp == 'một': temp = 'mốt'
                    speak.append(temp)
                    speak.append('mươi')
                else: speak.append('mừoi')
            elif t[i] == '1' and p == 1: speak.pop()
            elif t[i] != '1' and p == 1 and zero == 1: 
                temp = speak.pop()
                speak.pop()
                speak.append('mưoi')
                speak.append(temp)

            p += 1
        
        if l >= 4 and count == 0:
            speak.append('nghìn')
        elif l >= 7 and count == 1:
            speak.append('triệu')
        elif l >= 10 and count == 2:
            speak.append('tỷ')
    
    count += 1
    n = n[:-3]

print(copy_n, ':', end=' ')
for i in range(len(speak)-1, -1, -1):
    print(speak[i], end=' ')


    