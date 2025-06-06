#!/usr/bin/env python3
"""
Least Common Multiple (LCM) calculation utility function
"""


def gcd(a, b):
    """Helper function to calculate Greatest Common Divisor."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    Calculates the Least Common Multiple (LCM) of two integers.
    
    The LCM is the smallest positive integer that is divisible by both a and b.
    
    Args:
        a (int): First integer
        b (int): Second integer
    
    Returns:
        int: The least common multiple of a and b
        
    Raises:
        TypeError: If inputs are not integers
        ValueError: If either number is 0
        
    Examples:
        >>> lcm(4, 6)
        12
        >>> lcm(15, 25)
        75
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Both arguments must be integers")
    
    if a == 0 or b == 0:
        raise ValueError("LCM with 0 is undefined")
    
    # Convert to absolute values
    a, b = abs(a), abs(b)
    
    # LCM = (a * b) / gcd(a, b)
    return (a * b) // gcd(a, b)


if __name__ == "__main__":
    # Example usage
    print(lcm(4, 6))  # 12
    print(lcm(15, 25))  # 75
