
### 1. Delimiters in SQL
Delimiters are symbols or keywords used to separate statements in SQL. The most common delimiter is the semicolon (`;`), which signifies the end of a SQL statement. However, different SQL tools and databases might allow or require different delimiters, especially when working with scripts or stored procedures that contain multiple statements.

#### Example
In MySQL, you often need to change the delimiter when creating stored procedures or functions to differentiate the end of a procedure from the end of a single SQL statement:

```sql
DELIMITER $$

CREATE PROCEDURE myProcedure()
BEGIN
   -- SQL statements here
   SELECT * FROM myTable;
END $$

DELIMITER ;
```

In this example, the delimiter is changed to `$$` to allow the procedure's definition to contain semicolons without ending the procedure.

### 2. Deterministic Functions in SQL
A deterministic function always returns the same result given the same input parameters. This is in contrast to non-deterministic functions, which might return different results for the same inputs due to factors like internal state or external conditions (e.g., current date/time).

#### Example
In MySQL, you can specify that a user-defined function is deterministic using the `DETERMINISTIC` keyword:

```sql
CREATE FUNCTION addNumbers(x INT, y INT)
RETURNS INT
DETERMINISTIC
BEGIN
   RETURN x + y;
END;
```

This function is deterministic because it will always return the same result for the same `x` and `y` values.

### 3. Stored Procedures in SQL
Stored procedures are a set of SQL statements that can be executed as a program. They allow for modular programming and can include control-flow logic like IF statements, loops, and exception handling.

#### Example
Creating a simple stored procedure in MySQL:

```sql
DELIMITER $$

CREATE PROCEDURE getEmployeeById(IN emp_id INT)
BEGIN
   SELECT * FROM employees WHERE id = emp_id;
END $$

DELIMITER ;
```

In this example, the procedure `getEmployeeById` takes an employee ID as an input parameter and selects the corresponding record from the `employees` table.

### Benefits of Stored Procedures
1. **Performance**: Stored procedures can improve performance by reducing the amount of data transferred between the application and the database server.
2. **Security**: They can encapsulate business logic on the server side, preventing direct access to the underlying data.
3. **Maintainability**: Procedures promote code reuse and centralize business logic, making maintenance easier.

### Using Deterministic Functions within Procedures
When using deterministic functions within stored procedures, you can optimize performance and ensure consistent results, particularly important for complex calculations or data transformations.

### Example: Using a Deterministic Function in a Procedure
```sql
DELIMITER $$

CREATE FUNCTION calculateDiscount(price DECIMAL, discountRate DECIMAL)
RETURNS DECIMAL
DETERMINISTIC
BEGIN
   RETURN price * (1 - discountRate);
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE applyDiscount(IN productId INT, IN discountRate DECIMAL)
BEGIN
   UPDATE products
   SET price = calculateDiscount(price, discountRate)
   WHERE id = productId;
END $$

DELIMITER ;
```

In this example, the `calculateDiscount` function is deterministic and is used within the `applyDiscount` procedure to update product prices.

By understanding and utilizing delimiters, deterministic functions, and stored procedures, you can write more efficient, maintainable, and secure SQL code.