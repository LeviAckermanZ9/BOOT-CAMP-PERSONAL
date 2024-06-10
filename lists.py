# Notes:
# A list is an ordered, mutable collection of items.
# Lists can contain elements of different data types.
# Lists are defined using square brackets [].

# Common Operations:
# Creating a list
my_list = [1, 2, 3, 4]

# Accessing elements
print(my_list[0])  # Output: 1

# Slicing a list
print(my_list[1:3])  # Output: [2, 3]

# Adding elements
my_list.append(5)
print(my_list)  # Output: [1, 2, 3, 4, 5]

my_list.insert(2, 10)
print(my_list)  # Output: [1, 2, 10, 3, 4, 5]

# Removing elements
my_list.remove(3)
print(my_list)  # Output: [1, 2, 10, 4, 5]

my_list.pop()
print(my_list)  # Output: [1, 2, 10, 4]

# List comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Algorithm 1: Find the maximum value in a list
def find_maximum(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

# Example usage
numbers = [1, 5, 2, 9, 3]
print(find_maximum(numbers))  # Output: 9