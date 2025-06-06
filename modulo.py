#!/usr/bin/env python3
"""
Modulo (remainder) calculation utility function
"""


def modulo(a, b):
    """
    Calculates the remainder when dividing the first number by the second.
    
    Args:
        a (int or float): The dividend
        b (int or float): The divisor
    
    Returns:
        int or float: The remainder of the division
        
    Raises:
        ZeroDivisionError: If the divisor is zero
        
    Examples:
        >>> modulo(10, 3)
        1
        >>> modulo(10.5, 3)
        1.5
    """
    if b == 0:
        raise ZeroDivisionError("Modulo by zero is not allowed")
    
    return a % b


if __name__ == "__main__":
    # Example usage
    print(modulo(10, 3))  # 1
    print(modulo(10.5, 3))  # 1.5
