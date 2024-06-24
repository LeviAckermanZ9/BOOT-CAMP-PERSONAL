Control Language (TCL) in SQL is used to manage transactions in a database. Transactions are a sequence of SQL operations performed as a single logical unit of work. TCL commands ensure that these operations are executed in a controlled manner to maintain the integrity and consistency of the database.

### Key TCL Commands

1. **BEGIN TRANSACTION / START TRANSACTION**
2. **COMMIT**
3. **ROLLBACK**
4. **SAVEPOINT**
5. **SET TRANSACTION**

#### 1. BEGIN TRANSACTION / START TRANSACTION
This command marks the beginning of a transaction. It sets a point from which the SQL statements are executed as a single unit.

```sql
START TRANSACTION;
-- Or, in some systems
BEGIN TRANSACTION;
```

#### 2. COMMIT
The `COMMIT` command is used to save all the changes made during the current transaction to the database. Once a transaction is committed, it cannot be undone.

```sql
COMMIT;
```

#### Example
```sql
START TRANSACTION;

UPDATE accounts
SET balance = balance - 100
WHERE account_id = 1;

UPDATE accounts
SET balance = balance + 100
WHERE account_id = 2;

COMMIT;
```

In this example, money is transferred from one account to another. The changes are saved only after the `COMMIT` command.

#### 3. ROLLBACK
The `ROLLBACK` command undoes all the changes made during the current transaction. It reverts the database to the state it was in before the transaction began.

```sql
ROLLBACK;
```

#### Example
```sql
START TRANSACTION;

UPDATE accounts
SET balance = balance - 100
WHERE account_id = 1;

UPDATE accounts
SET balance = balance + 100
WHERE account_id = 2;

-- Suppose an error occurs here
ROLLBACK;
```

If an error occurs during the transaction, the `ROLLBACK` command undoes all the changes made.

#### 4. SAVEPOINT
The `SAVEPOINT` command sets a point within a transaction to which you can later roll back. This allows partial rollback of a transaction.

```sql
SAVEPOINT savepoint_name;
```

#### Example
```sql
START TRANSACTION;

UPDATE accounts
SET balance = balance - 100
WHERE account_id = 1;

SAVEPOINT halfway;

UPDATE accounts
SET balance = balance + 100
WHERE account_id = 2;

-- Suppose an error occurs here
ROLLBACK TO halfway;

COMMIT;
```

In this example, if an error occurs after the `SAVEPOINT`, the transaction can be rolled back to the `SAVEPOINT`, not all the way to the beginning.

#### 5. SET TRANSACTION
The `SET TRANSACTION` command is used to set the characteristics of the current transaction, such as the isolation level.

```sql
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

#### Example
```sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

START TRANSACTION;

-- Transaction operations here

COMMIT;
```

### Transaction Properties (ACID)
Transactions are designed to have four key properties known as ACID:

1. **Atomicity**: Ensures that all operations within a transaction are completed successfully. If any operation fails, the entire transaction fails and the database is left unchanged.
2. **Consistency**: Ensures that a transaction brings the database from one valid state to another, maintaining database invariants.
3. **Isolation**: Ensures that transactions are isolated from one another. Changes made by a transaction are not visible to other transactions until the transaction is committed.
4. **Durability**: Ensures that once a transaction has been committed, it will remain so, even in the event of a system failure.

### Practical Example
Consider a banking application where money is transferred from one account to another:

```sql
-- Start the transaction
START TRANSACTION;

-- Deduct from sender's account
UPDATE accounts
SET balance = balance - 500
WHERE account_id = 1;

-- Add to receiver's account
UPDATE accounts
SET balance = balance + 500
WHERE account_id = 2;

-- Commit the transaction if everything is correct
COMMIT;

-- If there's an error at any point, rollback the transaction
ROLLBACK;
```

In this example, if any of the updates fail, the `ROLLBACK` command will ensure that neither account's balance is changed.

# THANK YOU