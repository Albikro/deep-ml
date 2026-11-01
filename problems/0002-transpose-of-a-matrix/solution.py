def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    

    if not a:
        return []
    else:
        m = len(a) #row number
        n = len(a[0]) #column number
        return [[row[i] for row in a] for i in range(n)]



        