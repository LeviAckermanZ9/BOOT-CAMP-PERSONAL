```python
listbox = tk.Listbox(root)
listbox.pack()
for item in ["Item 1", "Item 2", "Item 3"]:
    listbox.insert(tk.END, item)
```

#### 8. **Scrollbar**
   - **Purpose**: Adds a vertical or horizontal scrollbar to another widget.
   - **Common Options**: `orient` (vertical or horizontal), `command`.

   ```python
   scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
   scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

   listbox.config(yscrollcommand=scrollbar.set)
   scrollbar.config(command=listbox.yview)
   ```

#### 9. **Checkbutton**
   - **Purpose**: Represents a binary state (checked or unchecked).
   - **Common Options**: `text`, `variable` (usually a `tk.IntVar`).

   ```python
   var = tk.IntVar()
   checkbutton = tk.Checkbutton(root, text="Check me", variable=var)
   checkbutton.pack()
   ```

#### 10. **Radiobutton**
   - **Purpose**: Allows the user to select one option from a set.
   - **Common Options**: `text`, `variable` (usually a `tk.StringVar` or `tk.IntVar`), `value`.

   ```python
   var = tk.StringVar(value="Option 1")
   radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1")
   radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2")
   radiobutton1.pack()
   radiobutton2.pack()
   ```

#### 11. **Scale**
   - **Purpose**: Slider for selecting a numerical value.
   - **Common Options**: `from_`, `to`, `orient` (horizontal or vertical), `variable`.

   ```python
   scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
   scale.pack()
   ```

#### 12. **Spinbox**
   - **Purpose**: Entry widget with increment and decrement arrows.
   - **Common Options**: `from_`, `to`, `increment`.

   ```python
   spinbox = tk.Spinbox(root, from_=0, to=10)
   spinbox.pack()
   ```

#### 13. **Menu**
   - **Purpose**: Creates menus and submenus for the application.
   - **Common Options**: `tearoff`, `label`, `command`.

   ```python
   menu = tk.Menu(root)
   root.config(menu=menu)

   submenu = tk.Menu(menu, tearoff=0)
   menu.add_cascade(label="File", menu=submenu)
   submenu.add_command(label="Open", command=lambda: print("Open clicked"))
   submenu.add_command(label="Save", command=lambda: print("Save clicked"))
   ```

#### 14. **Message**
   - **Purpose**: Displays multiline text messages.
   - **Common Options**: `text`, `bg`, `fg`, `font`.

   ```python
   message = tk.Message(root, text="This is a message widget.", width=200)
   message.pack()
   ```

#### 15. **Toplevel**
   - **Purpose**: Creates a new top-level window.
   - **Common Options**: Same as for the main window (e.g., `title`, `geometry`).

   ```python
   toplevel = tk.Toplevel(root)
   toplevel.title("New Window")
   ```

### Example of Using Multiple Widgets Together


```python
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Widget Example")

# Label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

# Entry
entry = tk.Entry(root)
entry.pack(pady=10)

# Button
def on_button_click():
    label.config(text=f"Hello, {entry.get()}")

button = tk.Button(root, text="Greet", command=on_button_click)
button.pack(pady=10)

# Checkbutton
var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Check me", variable=var)
checkbutton.pack(pady=10)

# Radiobutton
var = tk.StringVar(value="Option 1")
radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1")
radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2")
radiobutton1.pack()
radiobutton2.pack()

# Scale
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack(pady=10)

# Listbox with Scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

for i in range(1, 101):
    listbox.insert(tk.END, f"Item {i}")

# Run the application
root.mainloop()
```

# THANK YOU