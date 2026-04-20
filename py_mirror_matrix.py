def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    n = 0
    for lst in matrix:
        lst = sorted(lst, reverse=True)
        matrix[n] = lst
        n += 1

    return matrix
