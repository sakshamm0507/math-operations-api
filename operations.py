from google import genai
from google.genai import types
import add, subtract, multiply, divide, power, modulo, factorial, gcd, lcm, geometric_mean, matrix_operations

# Register your functions
tools = [
    add.add, 
    subtract.subtract, 
    multiply.multiply, 
    divide.divide, 
    power.power, 
    modulo.modulo, 
    factorial.factorial, 
    gcd.gcd, 
    lcm.lcm, 
    geometric_mean.geometric_mean,
    matrix_operations.matrix_add
    # Add other matrix operations as needed
]

# Configure Gemini client
# Get API key from environment variable
import os
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY environment variable not set.")
    print("Please set it with: $env:GEMINI_API_KEY='your-api-key'")
    exit(1)
client = genai.Client(api_key=api_key)
config = types.GenerateContentConfig(tools=tools)

while True:
    user_input = input("Enter your calculation (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    # Send the user's input to Gemini
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_input,
        config=config
    )

    print("Result:", response.text)
