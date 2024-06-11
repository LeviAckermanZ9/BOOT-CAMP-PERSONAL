
### Basic "Hello, World!" Example

Here's a simple Tkinter application that displays a window with a label saying "Hello, World!".

```python
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello, World!")

# Create a label widget with text "Hello, World!"
label = tk.Label(root, text="Hello, World!")
label.pack(pady=20)

# Run the application

root.mainloop() 
