# Python Input and Output Statements

# Input statement
age = input("Enter your age: ")
print("You are", age, "years old")

# Output statement with keyword arguments
print("Python", "Programming", sep=" - ", end="!!!\n")

# Data Types in Python
int_num = 42
float_num = 2.718
complex_num = 1 + 4j
string = "Python Rocks!"
boolean = False
list_example = ["apple", "banana", "cherry"]
tuple_example = (7, 8, 9)
dict_example = {"city": "New York", "population": 8400000}
set_example = {"a", "b", "c"}

print(int_num, float_num, complex_num)
print(string, boolean)
print(list_example, tuple_example)
print(dict_example, set_example)

# Expressions and Operators

x = 15
y = 4

# Arithmetic Operators
print(x + y)  # Addition: 19
print(x - y)  # Subtraction: 11
print(x * y)  # Multiplication: 60
print(x / y)  # Division: 3.75
print(x // y) # Floor Division: 3
print(x % y)  # Modulus: 3
print(x ** y) # Exponentiation: 50625

# Comparison Operators
print(x == y) # Equal to: False
print(x != y) # Not equal to: True
print(x > y)  # Greater than: True
print(x < y)  # Less than: False
print(x >= y) # Greater than or equal to: True
print(x <= y) # Less than or equal to: False

# Logical Operators
print(x > 10 and y < 10)  # and: True
print(x > 20 or y < 10)   # or: True
print(not(x > 10 and y < 10)) # not: False

# Type Casting
float_from_str = float("3.14")
int_from_bool = int(True)
str_from_list = str([1, 2, 3])
tuple_from_set = tuple({1, 2, 3})
set_from_tuple = set((1, 2, 3, 1))

print(float_from_str)
print(int_from_bool)
print(str_from_list)
print(tuple_from_set)
print(set_from_tuple)

# Conditional Statements
temperature = 30

if temperature > 35:
    print("It's very hot")
elif temperature > 25:
    print("It's warm")
else:
    print("It's cool")

# Looping Statements
# For loop
numbers = [10, 20, 30, 40]
for number in numbers:
    print(number)

# While loop
counter = 3
while counter > 0:
    print(counter)
    counter -= 1

# Jumping Statements
# break statement
for n in range(10):
    if n == 6:
        break
    print(n)

# continue statement
for n in range(10):
    if n % 2 == 0:
        continue
    print(n)

# Special Functions
# len() function
length_of_string = len("Hello, World!")
print("Length of string:", length_of_string)

# id() function
unique_id = id("Python")
print("Unique ID of 'Python':", unique_id)

# type() function
type_of_variable = type(3.14)
print("Type of 3.14:", type_of_variable)

# range() function
range_example = range(1, 10, 2)
print("Range example:", list(range_example))
