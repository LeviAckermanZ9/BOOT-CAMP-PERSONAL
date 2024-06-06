# Functions in Python

# 1. Syntax of a Function
def say_hello(name):
    """This function prints a hello message."""
    print("Hello", name + "!")

# Function call
say_hello("John")

# 2. Parameters in Functions
def multiply(x, y):
    """This function returns the product of two numbers."""
    return x * y

# Positional arguments
result = multiply(4, 5)
print(result)

# Keyword arguments
result = multiply(x=4, y=5)
print(result)

# 3. Return Statement
def cube(n):
    """This function returns the cube of a number."""
    return n ** 3

# Function call
result = cube(3)
print(result)

# 4. Default Parameters
def greet(name, greeting="Hello"):
    """This function prints a greeting message."""
    print(greeting, name + "!")

# Calling with both arguments
greet("Emma", "Hi")

# Calling with only the required argument
greet("Emma")

# 5. Variable-Length Arguments
def sum_numbers(*args):
    """This function returns the sum of all arguments."""
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15

def print_info(**kwargs):
    """This function prints key-value pairs."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(firstname="John", lastname="Doe", age=30)

# 6. Lambda Functions
# Lambda function to subtract two numbers
subtract = lambda a, b: a - b

# Calling the lambda function
print(subtract(10, 4))  # Output: 6

# Lambda function for mapping
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16]

# 7. Function Annotations
def add_numbers(a: int, b: int) -> int:
    """This function adds two numbers."""
    return a + b

# Calling the function
print(add_numbers(10, 20))

# 8. Recursion
def fibonacci(n):
    """This function returns the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Function call
print(fibonacci(6))  # Output: 8

# 9. Scope of Variables
def bar():
    """This function demonstrates local scope."""
    y = 15
    print("Inside function:", y)

y = 25
bar()
print("Outside function:", y)  # This will not affect the value of y inside the function
