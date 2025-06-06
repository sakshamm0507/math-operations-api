#!/usr/bin/env python3
"""
Division utility function
"""


def divide(a, b, decimal_places=None):
    """
    Divides the first number by the second number.
    
    Args:
        a (float or int): The dividend (numerator)
        b (float or int): The divisor (denominator)
        decimal_places (int, optional): Number of decimal places to round to.
                                       If None, no rounding is performed.
    
    Returns:
        float or int: The quotient after division
        
    Raises:
        ZeroDivisionError: If the divisor is zero
        
    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(10, 3, 2)
        3.33
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    
    result = a / b
    
    if decimal_places is not None:
        result = round(result, decimal_places)
        
    return result


if __name__ == "__main__":
    # Example usage
    print(divide(10, 2))  # 5.0
    print(divide(10, 3, 2))  # 3.33
