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
print("\n--- Other Basic Concepts ---")

# Lists and loops
fruits = ["apple", "banana", "orange", "grape"]
print("Fruits in the list:")
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")

# Dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"\nPerson info: {person['name']} is {person['age']} years old and lives in {person['city']}")

# Simple function with conditional
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

print(check_even_odd(7))
print(check_even_odd(12))