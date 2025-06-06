#!/usr/bin/env python3
"""
Multiplication utility function
"""


def multiply(*numbers):
    """
    Multiplies two or more numbers together.
    
    Args:
        *numbers: Variable length argument list of numbers to be multiplied
    
    Returns:
        float or int: The product of all input numbers
        
    Raises:
        ValueError: If no arguments are provided
        
    Examples:
        >>> multiply(2, 3)
        6
        >>> multiply(2, 3, 4)
        24
    """
    if not numbers:
        raise ValueError("At least one number must be provided")
    
    result = 1
    for num in numbers:
        result *= num
    return result


if __name__ == "__main__":
    # Example usage
    print(multiply(2, 3))  # 6
    print(multiply(2, 3, 4))  # 24
