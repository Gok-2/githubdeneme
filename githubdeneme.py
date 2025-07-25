# Basic Python Program - Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

# Main program
print("Welcome to Simple Calculator!")
print("Operations: +, -, *, /")

# Get user input
try:
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    # Perform calculation
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        result = "Error: Invalid operation"
    
    print(f"Result: {result}")
    
except ValueError:
    print("Error: Please enter valid numbers")

# Example of other basic Python concepts
print("\nVibeCodingTR")