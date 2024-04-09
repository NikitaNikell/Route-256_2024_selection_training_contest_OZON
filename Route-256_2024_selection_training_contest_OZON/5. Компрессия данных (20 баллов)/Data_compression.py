import sys


def main():
    n = int(sys.stdin.readline())
    # print(n)
    for i in range(n):
        run_case()


def run_case():
    k = int(sys.stdin.readline())
    # print(k)
    arr = list(map(int, sys.stdin.readline().split()))
    # print(arr)
    res = compress(arr)
    print(len(res))
    print(' '.join(map(str, res)))


def compress(arr):
    if len(arr) == 1:
        return [arr[0], 0]
    res = []
    ci = 0
    temp = arr[0]
    toWrite = temp
    for i, v in enumerate(arr):
        if i == 0:
            continue
        if (ci <= 0) and v + 1 == temp:
            ci -= 1
            if i == len(arr) - 1:
                res.extend([toWrite, ci])
            temp -= 1
            continue
        if (ci >= 0) and v - 1 == temp:
            ci += 1
            if i == len(arr) - 1:
                res.extend([toWrite, ci])
            temp += 1
            continue
        if ci != 0:
            res.extend([toWrite, ci])
            ci = 0
            temp = v
            toWrite = temp
            if i + 1 == len(arr):
                res.extend([v, 0])
            continue
        res.extend([toWrite, 0])
        if i + 1 != len(arr):
            toWrite = v
            temp = v
        else:
            res.extend([v, 0])
    return res


if __name__ == "__main__":
    main()


