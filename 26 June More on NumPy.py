
### Broadcasting
Broadcasting allows NumPy to perform element-wise operations on arrays of different shapes.
1. **Broadcasting rules:**
    ```python
    array1 = np.array([1, 2, 3])
    array2 = np.array([[0], [1], [2]])
    print(array1 + array2)  # Adds each element of array1 to each row of array2
    ```

### Fancy Indexing and Boolean Indexing
Fancy and Boolean indexing are powerful ways to access and modify array elements.

1. **Fancy Indexing:**
    ```python
    array = np.arange(10)
    indices = [1, 3, 5]
    print(array[indices])
    array[indices] = 99
    print(array)
    ```

2. **Boolean Indexing:**
    ```python
    array = np.array([1, 2, 3, 4, 5])
    mask = array > 3
    print(array[mask])
    array[mask] = 0
    print(array)
    ```

### Advanced Array Manipulation
1. **Concatenation and Splitting:**
    ```python
    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])
    concatenated = np.concatenate((array1, array2))
    print(concatenated)
    
    array = np.array([1, 2, 3, 4, 5, 6])
    split = np.split(array, 3)
    print(split)
    ```

2. **Stacking Arrays:**
    ```python
    array1 = np.array([[1, 2], [3, 4]])
    array2 = np.array([[5, 6], [7, 8]])
    vertical_stack = np.vstack((array1, array2))
    horizontal_stack = np.hstack((array1, array2))
    print(vertical_stack)
    print(horizontal_stack)
    ```

3. **Tile and Repeat:**
    ```python
    array = np.array([1, 2, 3])
    tiled = np.tile(array, 2)
    repeated = np.repeat(array, 2)
    print(tiled)
    print(repeated)
    ```

### Random Number Generation
NumPy provides a suite of functions for generating random numbers.

1. **Basic Random Numbers:**
    ```python
    random_array = np.random.random((3, 3))
    print(random_array)
    ```

2. **Random Integers:**
    ```python
    random_integers = np.random.randint(0, 10, (3, 3))
    print(random_integers)
    ```

3. **Random Normal Distribution:**
    ```python
    normal_dist = np.random.normal(0, 1, (3, 3))  # Mean 0, Std 1
    print(normal_dist)
    ```

### Linear Algebra Operations
More advanced linear algebra operations are supported through the `np.linalg` module.

1. **Eigenvalues and Eigenvectors:**
    ```python
    matrix = np.array([[1, 2], [2, 1]])
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    print(eigenvalues)
    print(eigenvectors)
    ```

2. **Singular Value Decomposition (SVD):**
    ```python
    matrix = np.array([[1, 2], [3, 4], [5, 6]])
    U, S, Vt = np.linalg.svd(matrix)
    print(U)
    print(S)
    print(Vt)
    ```

3. **Solving Linear Systems:**
    ```python
    A = np.array([[3, 1], [1, 2]])
    b = np.array([9, 8])
    x = np.linalg.solve(A, b)
    print(x)
    ```

### Performance Tips
1. **Vectorization:**
    NumPy operations are vectorized, meaning they are implemented in C and perform faster than standard Python loops.
    ```python
    array = np.arange(1000000)
    %timeit array + 1  # Fast, vectorized operation
    ```

2. **Avoid Python loops for array operations:**
    ```python
    # Inefficient
    array = np.arange(1000000)
    for i in range(len(array)):
        array[i] += 1
    
    # Efficient
    array = np.arange(1000000)
    array += 1  # Vectorized operation
    ```

### Structured Arrays
Structured arrays allow you to use heterogeneously-typed data.

1. **Creating a Structured Array:**
    ```python
    data = np.array([(1, 'A', 2.5), (2, 'B', 3.6)],
                    dtype=[('id', 'i4'), ('name', 'U10'), ('value', 'f4')])
    print(data['id'])
    print(data['name'])
    print(data['value'])
    ```

### More Utilities
1. **Unique Elements:**
    ```python
    array = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    unique_elements = np.unique(array)
    print(unique_elements)
    ```

2. **Sorting Arrays:**
    ```python
    array = np.array([3, 1, 2, 5, 4])
    sorted_array = np.sort(array)
    print(sorted_array)
    ```

3. **Saving and Loading Arrays:**
    ```python
    array = np.array([1, 2, 3, 4, 5])
    np.save('array.npy', array)
    loaded_array = np.load('array.npy')
    print(loaded_array)
    ```

### Conclusion
These examples cover a broad range of NumPy's capabilities, from basic array creation to advanced linear algebra operations. For more details, the [NumPy documentation ](https://numpy.org/doc/) is an excellent resource.

# THANK YOU