#!/usr/bin/env python3
"""
Power calculation utility function
"""


def power(base, exponent):
    """
    Raises a base number to the specified exponent.
    
    Args:
        base (float or int): The base number
        exponent (float or int): The exponent
    
    Returns:
        float or int: The result of base raised to the exponent
        
    Examples:
        >>> power(2, 3)
        8
        >>> power(2, -1)
        0.5
        >>> power(2, 0.5)
        1.4142135623730951
    """
    return base ** exponent


if __name__ == "__main__":
    # Example usage
    print(power(2, 3))  # 8
    print(power(2, -1))  # 0.5
    print(power(2, 0.5))  # 1.4142135623730951 (square root of 2)
