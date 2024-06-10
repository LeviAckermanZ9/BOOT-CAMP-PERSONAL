# Notes:
# A dictionary is an unordered collection of key-value pairs.
# Keys must be unique and immutable.
# Dictionaries are defined using curly braces {}.

# Common Operations:
# Creating a dictionary
my_dict = {"key1": "value1", "key2": "value2"}

# Accessing values
print(my_dict["key1"])  # Output: value1

# Adding or updating a key-value pair
my_dict["key3"] = "value3"
print(my_dict)  # Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Removing a key-value pair
del my_dict["key1"]
print(my_dict)  # Output: {'key2': 'value2', 'key3': 'value3'}

# Iterating through keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# key2: value2
# key3: value3

# Algorithm 2: Count the frequency of elements in a list using a dictionary
def count_frequency(items):
    frequency = {}
    for item in items:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

# Example usage
items = ["apple", "banana", "apple", "cherry", "banana", "banana"]
print(count_frequency(items))
# Output: {'apple': 2, 'banana': 3, 'cherry': 1}