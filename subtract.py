#!/usr/bin/env python3
"""
Subtraction utility function
"""


def subtract(a, b, *args):
    """
    Subtracts the second and all subsequent numbers from the first number.
    
    Args:
        a (float or int): The number to subtract from
        b (float or int): The first number to subtract
        *args: Additional numbers to subtract
    
    Returns:
        float or int: The result after subtraction
        
    Examples:
        >>> subtract(10, 5)
        5
        >>> subtract(20, 5, 3, 2)
        10
    """
    result = a - b
    for num in args:
        result -= num
    return result


if __name__ == "__main__":
    # Example usage
    print(subtract(10, 5))  # 5
    print(subtract(20, 5, 3, 2))  # 10
