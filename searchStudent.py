dictionary = {
    '1951060982': {'name': 'Le Thanh Son', 'point': 10},
    '1951061782': {'name': 'Le Huy Hung', 'point': 8.9},
    '1951060234': {'name': 'Nguyen Thanh Thao', 'point': 4},
    '1951062967': {'name': 'Tran Quoc Toan', 'point': 7.4},
    '1951060284': {'name': 'Bui Van Kien', 'point': 5.5},
    '1951060098': {'name': 'Le Thi Hoa', 'point': 9.1},
}

SBD = input('Nhap So Bao Danh cua hoc sinh:')

print('Thong Tin:', dictionary.get(SBD, 'Khong co SBD trong danh sach'))