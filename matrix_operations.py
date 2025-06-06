#!/usr/bin/env python3
"""
Matrix operations utility functions
"""


def matrix_add(matrix_a, matrix_b):
    """
    Adds two matrices of the same dimensions.
    
    Args:
        matrix_a (list of lists): First matrix represented as a list of rows
        matrix_b (list of lists): Second matrix represented as a list of rows
    
    Returns:
        list of lists: The resulting matrix after addition
        
    Raises:
        ValueError: If matrices have different dimensions
        
    Examples:
        >>> matrix_add([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[6, 8], [10, 12]]
    """
    # Check if matrices have the same dimensions
    if len(matrix_a) != len(matrix_b) or any(len(row_a) != len(row_b) for row_a, row_b in zip(matrix_a, matrix_b)):
        raise ValueError("Matrices must have the same dimensions for addition")
    
    # Perform addition
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    
    return result


def matrix_multiply(matrix_a, matrix_b):
    """
    Multiplies two matrices if their dimensions are compatible.
    
    Args:
        matrix_a (list of lists): First matrix represented as a list of rows
        matrix_b (list of lists): Second matrix represented as a list of rows
    
    Returns:
        list of lists: The resulting matrix after multiplication
        
    Raises:
        ValueError: If matrices have incompatible dimensions
        
    Examples:
        >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]
    """
    # Check if matrices can be multiplied
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Number of columns in first matrix must equal number of rows in second matrix")
    
    # Perform multiplication
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            element = 0
            for k in range(len(matrix_b)):
                element += matrix_a[i][k] * matrix_b[k][j]
            row.append(element)
        result.append(row)
    
    return result


if __name__ == "__main__":
    # Example usage
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    
    print("Matrix A + B:")
    print(matrix_add(A, B))  # [[6, 8], [10, 12]]
    
    print("Matrix A × B:")
    print(matrix_multiply(A, B))  # [[19, 22], [43, 50]]
