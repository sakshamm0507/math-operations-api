#!/usr/bin/env python3
"""
Addition utility function
"""


def add(*numbers):
    """
    Adds two or more numbers together.
    
    Args:
        *numbers: Variable length argument list of numbers to be added
    
    Returns:
        float or int: The sum of all input numbers
        
    Examples:
        >>> add(1, 2)
        3
        >>> add(1.5, 2.5, 3)
        7.0
    """
    return sum(numbers)


if __name__ == "__main__":
    # Example usage
    print(add(5, 10))  # 15
    print(add(1, 2, 3, 4, 5))  # 15
