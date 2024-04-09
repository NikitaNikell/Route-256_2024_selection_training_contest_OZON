def check_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def check_day(day, month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return True if day <= 31 else False
    elif month in [4, 6, 9, 11]:
        return True if day <= 30 else False
    elif month == 2:
        if check_year(year):
            if day > 29:
                return False
            else:
                return True
        else:
            if day > 28:
                return False
            else:
                return True


date = [list(map(int, input().split(" "))) for i in range(int(input()))]

for day, month, year in date:
    print("YES" if check_day(day, month, year) else "NO")

# Входные данные и ожидаемый результат
# 10
# 10 9 2022 YES
# 21 9 2022 YES
# 29 2 2022 NO
# 31 2 2022 NO
# 29 2 2000 YES
# 29 2 2100 NO
# 31 11 1999 NO
# 31 12 1999 YES
# 29 2 2024 YES
# 29 2 2023 NO
