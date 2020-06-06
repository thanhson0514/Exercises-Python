def test(n):
    # n = int(input('Nhập số: '))
    # # kiem tra so khong vuot qua 9 chu so
    # while len(str(n)) > 10:
    #     print('Số nguyên không được lớn hơn 9 chữ số. Mời nhập lại:')
    #     n = int(input())

    n = str(int(n))
    l = len(n)
    copy_n = n
    number = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']
    speak = []
    count = 0

    # neu nhap bang khong thi in ra ket qua
    if n == '0' and l == 1: print('không')
    while n != '':
        # chia so ra de lay 3 chu so
        t = n[-3:]

        # kiem tra xem 3 chu so do co la 3 chu so khong
        # dieu kien kiem tra cac so nhu 1000,10000,100000 ....
        if int(t) == 0:
            if l >= 4 and count == 0: speak.append('nghìn')
            elif l >= 7 and count == 1:
                temp = speak.pop()
                # kiem tra xem phia truoc co hang nghin hay khong
                if temp != 'nghìn': speak.append(temp)
                speak.append('triệu')
            elif l >= 10 and count == 2:
                temp = speak.pop()
                # kiem tra xem phia truoc co hang trieu hay khong
                if temp != 'triệu': speak.append(temp)
                speak.append('tỷ')
        else:
            zero = 0
            p = 0
            
            for i in range(len(t)-1,-1,-1):
                # kiem tra xem chu so co do dai la 3 chu so hay khong 
                # neu do dai 3 chu so doc la tram
                if p == 2 and l > 2: speak.append('trăm')
                speak.append(number[int(t[i])])
                # kiem tra chu so hang don vi co phai la khong hay khong
                # neu la khong thi doc la muoi
                # if t[i] == '5' and p == 0 and l > 1: 
                #     speak.pop()
                #     speak.append('lăm')
                if t[i] == '5' and p == 0 and l > 2: 
                    speak.pop()
                    speak.append('lăm')
                elif t[i] == '0' and p == 0:
                    speak.pop()
                    speak.append('mười')
                    # kiem tra so khong
                    zero += 1
                
                # kiem tra xem chu so thu 2 (hang chuc) co phai la so khong hay khong
                # 1. Neu la so khong va co tu 3 chu so chu thi doc la le
                # 2. neu la so mot thi doc la muoi
                # 3. neu khong phai so khong va so mot thi doc them muoi truoc hang don vi
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
                    # dieu kien xu ly phan tieng viet cua cach doc muoi
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

                # tang so lan kiem tra
                p += 1
            
            # dieu kien kiem tra xem so co bao nhieu chu so de doc them thanh phan
            if l >= 4 and count == 0:
                speak.append('nghìn')
            elif l >= 7 and count == 1:
                speak.append('triệu')
            elif l >= 10 and count == 2:
                speak.append('tỷ')
        
        count += 1
        # cat 3 chua so cuoi
        n = n[:-3]

    # in ra man hinh
    print(copy_n, ':', end=' ')
    for i in range(len(speak)-1, -1, -1):
        print(speak[i], end=' ')

    # C2:
    '''
        speak.reverse()
        print(' '.join(speak))
    '''

f = open('test.txt', 'r')
read = f.readlines()
f.close()

n = []
for i in read:    
    n.extend(i.split())
from random import randint
for i in range(50):
    rd = randint(0,1000000000)
    test(rd)
    print()