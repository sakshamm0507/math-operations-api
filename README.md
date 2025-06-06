# Mathematical Operations API

A Python-based API that provides various mathematical operations through Google's Gemini AI model.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Advanced mathematical functions (power, modulo, factorial)
- Number theory operations (GCD, LCM)
- Statistical operations (geometric mean)
- Matrix operations

## Requirements

- Python 3.6+
- Google Gemini API key

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install google-generativeai
   ```
3. Replace the API key in `operations.py` with your own Gemini API key

## Usage

Run the operations.py script:

```
python operations.py
```

Then enter your calculation when prompted. For example:
- "add 4 and 5"
- "what is the factorial of 5?"
- "calculate the GCD of 24 and 36"

Type 'exit' to quit the program.

## Functions

- `add`: Add two or more numbers
- `subtract`: Subtract numbers from a starting value
- `multiply`: Multiply two or more numbers
- `divide`: Divide numbers
- `power`: Raise a number to a power
- `modulo`: Calculate remainder after division
- `factorial`: Calculate the factorial of a number
- `gcd`: Find greatest common divisor
- `lcm`: Find least common multiple
- `geometric_mean`: Calculate geometric mean
- `matrix_add`: Add two matrices

## License

MIT
