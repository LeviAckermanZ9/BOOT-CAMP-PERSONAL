# try-except
try:
    num_list = [1, 2, 3]
    print(num_list[5])
except IndexError:
    print("Oops! Index out of range. Ensure you're accessing a valid index within the list.")

# Handling multiple exceptions 
try:
    user_input = input("Please enter an integer: ")
    result = int(user_input)
except ValueError:
    print("Error: Input must be a valid integer. Please try again.")

# Raising exceptions
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Invalid dimensions provided. Length and width must be positive values.")
    return length * width

try:
    area = calculate_area(-5, 4)
except ValueError as e:
    print("Error:", e)

# Custom exceptions
class OutOfStockError(Exception):
    pass

class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    
    def reduce_stock(self, amount):
        if amount > self.quantity:
            raise OutOfStockError(f"Error: Not enough {self.name} in stock.")
        self.quantity -= amount

item = Item("Apples", 5)
try:
    item.reduce_stock(10)
except OutOfStockError as e:
    print("Error:", e)

# Using finally
try:
    file = open("nonexistent_file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File not found. Please ensure the file exists.")
finally:
    print("Cleanup: Closing file if it was opened.")
