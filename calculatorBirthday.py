dd = int(input('Day:'))
mm = int(input('Month:'))
yy = int(input('Year:'))
static_year = 2020
check_day = check_month = check_year = False
index_day = [31,29,31,30,31,30,31,31,30,31,30,31]

while True:
    # kiem tra ngay hop le
    if dd >= 0 and dd <= index_day[mm-1]: check_day = True
    else: print('Ngay khong hop le', dd, '. Vui long thu lai!')

    # kiem tra thang hop le
    if mm >= 1 and mm <= 12: check_month = True
    else: print('Thang khong hop le', mm, '. Vui long thu lai')

    # kiem tra nam hop le
    if yy > 0 and yy <= 2021: 
        if dd == 1 and mm == 1 and yy == 2021: check_year = True
        elif yy > 0 and yy != 2021: check_year = True
        else: print('Bạn chỉ được nhập từ 1/1/2021 trở về trước.')
    else: print('Nam khong hop le', yy, '. Vui long thu lai')

    # neu hop le thi thoat
    if check_day and check_month and check_year: break

    # nhap lai
    dd = int(input('Day:'))
    mm = int(input('Month:'))
    yy = int(input('Year:'))


if dd == 1 and mm == 1:
    age = 2021 - yy
    total_day = 0
    total_month = 0

else:
    age = static_year - yy
    total_day = index_day[mm-1] - dd + 1
    total_month = 12 - mm

print(f'Tuoi: {age} nam {total_month} thang {total_day} ngay')