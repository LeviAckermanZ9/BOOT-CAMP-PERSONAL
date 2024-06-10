# Notes:
# A set is an unordered collection of unique elements.
# Sets are defined using curly braces {} or the set() function.
# Sets are mutable, but their elements must be immutable.

# Common Operations:
# Creating a set
my_set = {1, 2, 3, 4}
another_set = set([1, 2, 3, 4])

# Adding elements
my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Removing elements
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5}

# Checking membership
print(2 in my_set)  # Output: True
print(3 in my_set)  # Output: False

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
print(set_a | set_b)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(set_a & set_b)  # Output: {3}

# Difference
print(set_a - set_b)  # Output: {1, 2}

# Symmetric difference
print(set_a ^ set_b)  # Output: {1, 2, 4, 5}

# Algorithm 1: Remove duplicates from a list using a set
def remove_duplicates(input_list):
    return list(set(input_list))

# Example usage
input_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(input_list))  # Output: [1, 2, 3, 4, 5]

# Algorithm 2: Find common elements in two lists using sets
def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 & set2)

# Example usage
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(find_common_elements(list1, list2))  # Output: [3, 4]

# Algorithm 3: Find unique elements in a list using a set
def find_unique_elements(input_list):
    return list(set(input_list))

# Example usage
input_list = [1, 2, 2, 3, 4, 4, 5]
print(find_unique_elements(input_list))  # Output: [1, 2, 3, 4, 5]