#!/usr/bin/env python3
"""
Geometric mean calculation utility function
"""
import math


def geometric_mean(*numbers):
    """
    Calculates the geometric mean of a set of positive numbers.
    
    The geometric mean is the nth root of the product of n numbers.
    
    Args:
        *numbers: Variable length argument list of positive numbers
    
    Returns:
        float: The geometric mean of the input numbers
        
    Raises:
        ValueError: If any number is negative or if no numbers are provided
        
    Examples:
        >>> geometric_mean(2, 8)
        4.0
        >>> geometric_mean(1, 2, 4, 8)
        2.8284271247461903
    """
    if not numbers:
        raise ValueError("At least one number must be provided")
    
    for num in numbers:
        if num < 0:
            raise ValueError("All numbers must be non-negative")
    
    # Calculate the product of all numbers
    product = 1
    for num in numbers:
        product *= num
    
    # Calculate the nth root where n is the number of elements
    return product ** (1 / len(numbers))


if __name__ == "__main__":
    # Example usage
    print(geometric_mean(2, 8))  # 4.0
    print(geometric_mean(1, 2, 4, 8))  # ~2.83
