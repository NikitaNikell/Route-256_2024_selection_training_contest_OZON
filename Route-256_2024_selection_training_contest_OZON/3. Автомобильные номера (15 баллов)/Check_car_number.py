import re


def check_car_numbers(s):
    pattern = r'[A-Z]\d{2}[A-Z]{2}|[A-Z]\d[A-Z]{2}'
    elem = str(*s)
    matches = re.findall(pattern, elem)
    if ''.join(matches) == elem:
        return ' '.join(matches)
    else:
        return "-"


number_base = [list(map(str, input().split())) for _ in range(int(input()))]

for i in number_base:
    print(check_car_numbers(i))




