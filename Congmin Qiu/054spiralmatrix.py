def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    res = []

    num_row = len(matrix)
    if num_row == 0 or len(matrix[0]) == 0: return res
    num_col = len(matrix[0])

    row_s = 0
    row_e = num_row - 1
    col_s = 0
    col_e = num_col - 1

    while row_s <= row_e and col_s <= col_e:
        for i in range(col_s, col_e + 1):
            res.append(matrix[row_s][i])

        row_s += 1
        if row_s > row_e:
            break

        for i in range(row_s, row_e + 1):
            res.append(matrix[i][col_e])
        col_e = col_e - 1
        if col_s > col_e:
            break

        for i in range(col_e, col_s - 1, -1):
            res.append(matrix[row_e][i])
        row_e = row_e - 1
        if row_s > row_e:
            break

        for i in range(row_e, row_s - 1, -1):
            res.append(matrix[i][col_s])
        col_s += 1
        if col_s > col_e:
            break

    return res


m = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

res = spiralOrder(m)
print("")
