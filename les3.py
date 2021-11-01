def symmetric(lst):
    row = len(lst)

    if row == 0:
        return False

    col = len(lst[0])

    if row != col:
        return False

    for j in range(row):
        for i in range(col):
            if lst[j][i] != lst[i][j]:
                return False
    return True


if __name__ == "__main__":
    matrix_symm = [
        [1, 2, 3, 4, 5],
        [2, 1, 6, 7, 8],
        [3, 6, 1, 9, 10],
        [4, 7, 9, 1, 11],
        [5, 8, 10, 11, 1]
    ]

    matrix_unsymm = [
        [1, 2, 3, 4, 5],
        [2, 1, 6, 7, 8],
        [3, 6, 1, 9, 10],
        [4, 7, 9, 1, 11],
        [5, 8, 11, 11, 1]
    ]

    print(f'Is matrix symmetric? {symmetric(matrix_symm)}')
    print(f'Is matrix symmetric? {symmetric(matrix_unsymm)}')
