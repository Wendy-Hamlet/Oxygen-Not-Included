def hanoi_plus(n: int, x: str, y: str, z: str):
    if n == 1:
        print(f"{x}->{y}")
        print(f"{y}->{z}")
        return
    hanoi_plus(n - 1, x, y, z)
    print(f"{x}->{y}")
    hanoi_plus(n - 1, z, y, x)
    print(f"{y}->{z}")
    hanoi_plus(n - 1, x, y, z)


hanoi_plus(int(input("n")), input("x"), input("y"), input("z"))


def circle1(n: int):
    lst = [i for i in range(1, n + 1)]
    k = 1
    index = 0
    while len(lst) > 1:
        if k % 2 == 0:
            lst.pop(index)
        else:
            index += 1
        if index >= len(lst):
            index = 0
        k += 1
    return lst[0]


print(circle1(int(input("n"))))


def circle2(n: int):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2 * circle2(n // 2) - 1
    else:
        return 2 * circle2(n // 2) + 1


print(circle2(int(input("n"))))


def circle3(n: int):
    m = 0
    while not (2**m <= n and 2 ** (m + 1) > n):
        m += 1
    return 2 * (n - 2**m) + 1


print(circle3(int(input("n"))))


import pprint


def GridCover(k: int, i: int, j: int) -> list[list[int]]:
    d = {
        (1, 1): [[0, 4], [4, 4]],
        (1, 2): [[3, 0], [3, 3]],
        (2, 1): [[2, 2], [0, 2]],
        (2, 2): [[1, 1], [1, 0]],
    }
    if k == 1:
        return d[(i, j)]
    a, b = 0, 0
    if i > 2 ** (k - 1):
        i -= 2 ** (k - 1)
        a = 1
    if j > 2 ** (k - 1):
        j -= 2 ** (k - 1)
        b = 1
    judge = {(0, 0): 1, (0, 1): 2, (1, 0): 3, (1, 1): 4}
    spl = [[] for _ in range(4)]
    spl[judge[(a, b)] - 1] = GridCover(k - 1, i, j)
    if spl[0] == []:
        spl[0] = GridCover(k - 1, 2 ** (k - 1), 2 ** (k - 1))
        spl[0][2 ** (k - 1) - 1][2 ** (k - 1) - 1] = 5 - judge[(a, b)]
    if spl[1] == []:
        spl[1] = GridCover(k - 1, 2 ** (k - 1), 1)
        spl[1][2 ** (k - 1) - 1][0] = 5 - judge[(a, b)]
    if spl[2] == []:
        spl[2] = GridCover(k - 1, 1, 2 ** (k - 1))
        spl[2][0][2 ** (k - 1) - 1] = 5 - judge[(a, b)]
    if spl[3] == []:
        spl[3] = GridCover(k - 1, 1, 1)
        spl[3][0][0] = 5 - judge[(a, b)]
    return [spl[0][p] + spl[1][p] for p in range(2 ** (k - 1))] + [
        spl[2][p] + spl[3][p] for p in range(2 ** (k - 1))
    ]


pprint.pprint(GridCover(int(input("k")), int(input("i")), int(input("j"))))
