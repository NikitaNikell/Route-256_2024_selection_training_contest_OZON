def check_matrix(matrix):
    for m in matrix:
        one_ship = 4    # четыре однопалубных корабля;
        two_ship = 3    # три двухпалубных корабля;
        three_ship = 2  # два трёхпалубных корабля;
        four_ship = 1   # один четырёхпалубный корабль.
        print("YES" if m.count(1) == one_ship and m.count(2) == two_ship and m.count(3) == three_ship and m.count(4) == four_ship else "NO")


Matrix = [list(map(int, input().split())) for i in range(int(input()))]
check_matrix(Matrix)
