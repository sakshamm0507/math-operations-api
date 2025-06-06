#!/usr/bin/env python3
"""
Factorial calculation utility function
"""


def factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    
    Args:
        n (int): A non-negative integer
    
    Returns:
        int: The factorial of n (n!)
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
        
    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


if __name__ == "__main__":
    # Example usage
    print(factorial(5))  # 120
    print(factorial(0))  # 1
