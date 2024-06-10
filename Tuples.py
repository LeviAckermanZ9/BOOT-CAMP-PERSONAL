# Notes:
# A tuple is an ordered, immutable collection of items.
# Tuples can contain elements of different data types.
# Tuples are defined using parentheses ().

# Common Operations:
# Creating a tuple
my_tuple = (1, 2, 3, 4)

# Accessing elements
print(my_tuple[0])  # Output: 1

# Slicing a tuple
print(my_tuple[1:3])  # Output: (2, 3)

# Unpacking a tuple
(a, b, c, d) = my_tuple
print(a, b, c, d)  # Output: 1 2 3 4

# Note: Tuples are immutable, so elements cannot be added or removed.

# Algorithm 3: Swap two elements in a tuple (note: this creates a new tuple)
def swap_elements(tup, i, j):
    lst = list(tup)
    lst[i], lst[j] = lst[j], lst[i]
    return tuple(lst)

# Example usage
tup = (1, 2, 3, 4)
print(swap_elements(tup, 1, 3))  # Output: (1, 4, 3, 2)