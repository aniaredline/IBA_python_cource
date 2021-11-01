import random

row, col = 5, 5
matrix_ = [[random.randint(-1000, 1000) for _ in range(col)] for _ in range(row)]
matrix = [
    [1, 2, 3, 4, 5],
    [2, 1, 6, 7, 8],
    [3, 6, 1, 9, 10],
    [4, 7, 9, 1, 11],
    [5, 8, 10, 11, 1]
]


def symmetric(matrix):
    sym = True
    for j in range(row):
        for i in range(col):
            if matrix[j][i] != matrix[i][j]:
                sym = False
                break
        if not sym:
            break


print(sym)

if __name__ == "__name__":
    pass
