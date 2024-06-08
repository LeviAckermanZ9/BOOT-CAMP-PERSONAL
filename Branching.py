# Branching in Python is done using if, elif, and else statements
# It allows the program to take different paths based on conditions

# Example 1: Basic if-else branching
def check_even_odd(number):
    # Check if the number is even
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example 2: if-elif-else branching
def grade_score(score):
    # Check the score and assign a grade
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Example 3: Nested if statements
def check_age_category(age):
    # Determine the age category
    if age >= 0:
        if age < 13:
            return "Child"
        elif age < 20:
            return "Teenager"
        else:
            return "Adult"
    else:
        return "Invalid age"

# Example 4: Using branching in a loop to find prime numbers
def find_primes(n):
    primes = []
    for num in range(2, n + 1):
        # Assume number is prime until proven otherwise
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                # If num is divisible by any number other than 1 and itself, it is not prime
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Example 5: Using branching to implement a simple calculator
def simple_calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

# Example 6: Using branching to solve the FizzBuzz problem
def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        # Check multiple conditions with elif
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# Example 7: Using branching for error handling
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

# Testing the functions
print(check_even_odd(4))          # Output: Even
print(grade_score(85))            # Output: B
print(check_age_category(10))     # Output: Child
print(find_primes(20))            # Output: [2, 3, 5, 7, 11, 13, 17, 19]
print(simple_calculator(10, 5, "multiply"))  # Output: 50
print(fizz_buzz(15))              # Output: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
print(safe_divide(10, 0))         # Output: Cannot divide by zero