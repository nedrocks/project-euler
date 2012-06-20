"""Dang, this is messy. It works though."""

_MAPPING = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
}

count = 0

for i in xrange(1, 1001):
    list_num = list(str(i))
    if len(list_num) > 3:
        count += _MAPPING[int(list_num[0])] + len('thousand')
        list_num = list_num[1:]
    if len(list_num) > 2 and list_num[0] > '0':
        count += _MAPPING[int(list_num[0])]
        count += len('hundred')
        if list_num[1] > '0' or list_num[2] > '0':
            count += len('and')
        list_num = list_num[1:]
    if len(list_num) > 1 and list_num[0] > '0':
        if list_num[0] == '1':
            num = int(''.join(list_num))
            count += _MAPPING[num]
            list_num = []
        else:
            count += _MAPPING[int(list_num[0]) * 10]
            list_num = list_num[1:]
    if list_num and list_num[-1] > '0':
        if len(list_num) > 1:
            list_num = list_num[-1:]
        count += _MAPPING[int(list_num[0])]

print count

