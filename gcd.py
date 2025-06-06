#!/usr/bin/env python3
"""
Greatest Common Divisor (GCD) calculation utility function
"""


def gcd(a, b):
    """
    Calculates the Greatest Common Divisor (GCD) of two integers.
    
    Uses the Euclidean algorithm to find the largest positive integer
    that divides both a and b without a remainder.
    
    Args:
        a (int): First integer
        b (int): Second integer
    
    Returns:
        int: The greatest common divisor of a and b
        
    Raises:
        TypeError: If inputs are not integers
        ValueError: If both numbers are 0
        
    Examples:
        >>> gcd(48, 18)
        6
        >>> gcd(17, 13)
        1
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Both arguments must be integers")
    
    # Convert to absolute values
    a, b = abs(a), abs(b)
    
    if a == 0 and b == 0:
        raise ValueError("GCD of 0 and 0 is undefined")
    
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a


if __name__ == "__main__":
    # Example usage
    print(gcd(48, 18))  # 6
    print(gcd(17, 13))  # 1
