def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    m = len(a) #row number
    n = len(a[0]) #column number

    a_transpose = []
    for i in range(n):
        a_transpose.append([])
        for j in range(m):
            a_transpose[i].append(a[j][i])

    return a_transpose
        