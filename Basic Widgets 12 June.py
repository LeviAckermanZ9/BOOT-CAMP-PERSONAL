
### Basic Tkinter Widgets

#### 1. **Label**
   - **Purpose**: Displays static text or images.
   - **Common Options**: `text`, `image`, `bg` (background color), `fg` (foreground color), `font`.

   ```python
   label = tk.Label(root, text="This is a label")
   label.pack()
   ```

#### 2. **Button**
   - **Purpose**: Triggers a function or event when clicked.
   - **Common Options**: `text`, `command`, `bg`, `fg`, `font`.

   ```python
   def on_click():
       print("Button clicked!")
   
   button = tk.Button(root, text="Click Me", command=on_click)
   button.pack()
   ```

#### 3. **Entry**
   - **Purpose**: Single-line text input.
   - **Common Options**: `textvariable`, `show` (for passwords), `width`.

   ```python
   entry = tk.Entry(root)
   entry.pack()
   ```

#### 4. **Text**
   - **Purpose**: Multi-line text input.
   - **Common Options**: `height`, `width`, `bg`, `fg`, `font`.

   ```python
   text = tk.Text(root, height=10, width=30)
   text.pack()
   ```

#### 5. **Frame**
   - **Purpose**: Container for grouping and organizing other widgets.
   - **Common Options**: `bg`, `width`, `height`, `relief`.

   ```python
   frame = tk.Frame(root, bg="lightgray")
   frame.pack(fill=tk.BOTH, expand=True)
   ```

#### 6. **Canvas**
   - **Purpose**: Drawing shapes, images, and complex layouts.
   - **Common Options**: `bg`, `width`, `height`.

   ```python
   canvas = tk.Canvas(root, width=200, height=100)
   canvas.pack()
   canvas.create_rectangle(50, 25, 150, 75, fill="blue")
   ```

#### 7. **Listbox**
   - **Purpose**: Displays a list of items.
   - **Common Options**: `height`, `width`, `selectmode` (single, browse, multiple, extended).

   ```python
   listbox = tk.List