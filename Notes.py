# Notes:

# Lists:
# - A list is an ordered, mutable collection of items.
# - Lists can contain elements of different data types.
# - Lists are defined using square brackets [].
# - Common operations include:
#   - Creating a list: my_list = [1, 2, 3, 4]
#   - Accessing elements: my_list[0] (first element)
#   - Slicing a list: my_list[1:3] (elements from index 1 to 2)
#   - Adding elements: my_list.append(5) or my_list.insert(2, 10)
#   - Removing elements: my_list.remove(3) or my_list.pop()
#   - List comprehension: squares = [x**2 for x in range(5)]

# Tuples:
# - A tuple is an ordered, immutable collection of items.
# - Tuples can contain elements of different data types.
# - Tuples are defined using parentheses ().
# - Common operations include:
#   - Creating a tuple: my_tuple = (1, 2, 3, 4)
#   - Accessing elements: my_tuple[0] (first element)
#   - Slicing a tuple: my_tuple[1:3] (elements from index 1 to 2)
#   - Unpacking: a, b, c = my_tuple
# - Note: Tuples are immutable, so elements cannot be added or removed.

# Dictionaries:
# - A dictionary is an unordered collection of key-value pairs.
# - Keys must be unique and immutable.
# - Dictionaries are defined using curly braces {}.
# - Common operations include:
#   - Creating a dictionary: my_dict = {"key1": "value1", "key2": "value2"}
#   - Accessing values: my_dict["key1"]
#   - Adding or updating: my_dict["key3"] = "value3"
#   - Removing elements: del my_dict["key1"] or my_dict.pop("key2")
#   - Iterating through keys and values: for key, value in my_dict.items()

# Sets:
# - A set is an unordered collection of unique elements.
# - Sets are defined using curly braces {} or the set() function.
# - Sets are mutable, but their elements must be immutable.
# - Common operations include:
#   - Creating a set: my_set = {1, 2, 3, 4} or another_set = set([1, 2, 3, 4])
#   - Adding elements: my_set.add(5)
#   - Removing elements: my_set.remove(3)
#   - Checking membership: 2 in my_set
#   - Set operations:
#     - Union: set_a | set_b
#     - Intersection: set_a & set_b
#     - Difference: set_a - set_b
#     - Symmetric difference: set_a ^ set_b





# Lists:
# - Lists can be nested: nested_list = [[1, 2], [3, 4]]
# - Methods for lists include:
#   - .append(item) to add an item at the end
#   - .insert(index, item) to insert an item at a specific position
#   - .remove(item) to remove the first occurrence of an item
#   - .pop(index) to remove an item at a specific position
#   - .clear() to remove all items
#   - .index(item) to find the index of the first occurrence of an item
#   - .count(item) to count the number of occurrences of an item
#   - .sort() to sort the list in ascending order
#   - .reverse() to reverse the elements of the list in place

# Tuples:
# - Tuples support all operations that lists do except those that modify the tuple.
# - Methods for tuples include:
#   - .count(item) to count the number of occurrences of an item
#   - .index(item) to find the index of the first occurrence of an item
# - Tuples are often used for functions that return multiple values.

# Dictionaries:
# - Keys in dictionaries must be unique and of an immutable data type (e.g., strings, numbers, tuples).
# - Values can be of any data type and can be duplicated.
# - Methods for dictionaries include:
#   - .keys() to get all keys
#   - .values() to get all values
#   - .items() to get all key-value pairs
#   - .get(key, default) to get a value for a key, with an optional default if the key is not found
#   - .pop(key, default) to remove a key and return its value, with an optional default if the key is not found
#   - .popitem() to remove and return an arbitrary key-value pair
#   - .update(dict2) to update the dictionary with key-value pairs from another dictionary

# Sets:
# - Sets are useful for membership tests and eliminating duplicate entries.
# - Sets do not support indexing, slicing, or other sequence-like behavior.
# - Methods for sets include:
#   - .add(item) to add an item
#   - .remove(item) to remove an item (raises KeyError if not found)
#   - .discard(item) to remove an item (does nothing if not found)
#   - .pop() to remove and return an arbitrary item
#   - .clear() to remove all items
#   - .union(set2) to return a new set with all items from both sets
#   - .intersection(set2) to return a new set with only items common to both sets
#   - .difference(set2) to return a new set with items in the first set but not in the second
#   - .symmetric_difference(set2) to return a new set with items in either set but not both
#   - .issubset(set2) to check if the set is a subset of another set
#   - .issuperset(set2) to check if the set is a superset of another set
#   - .copy() to return a shallow copy of the set