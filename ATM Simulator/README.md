# ATM Simulator in Python

A **Command-Line ATM Simulator** built using **Python and Object-Oriented Programming (OOP)**.
This project simulates basic banking operations such as account creation, login authentication, deposits, withdrawals, balance checking, transaction history, and PIN management.

The system stores all account data in a **JSON database**, allowing persistent storage between program executions.

---

# Project Features

### 1. Account Creation

Users can create a new bank account by providing:

* First name
* Surname
* Mobile number
* PIN

The system automatically generates a **unique 9-digit account number**.

---

### 2. Secure Login System

Users must log in using:

* Account Number
* PIN

Security features include:

* Maximum **3 login attempts**
* Account automatically **blocked after 3 incorrect PIN attempts**

---

### 3. Deposit Money

Users can deposit money into their account.

After deposit:

* Balance is updated
* Transaction is recorded in transaction history

Example record:

```
Deposited : 500
```

---

### 4. Withdraw Money

Users can withdraw money if sufficient balance exists.

System checks:

* Withdrawal amount must be positive
* Account must have sufficient funds

Example record:

```
Withdrawn : 200
```

---

### 5. Balance Checking

Users can view their current account balance instantly.

Example output:

```
Your account Balance is : 1300
```

---

### 6. Transaction History

All transactions are stored and displayed to the user.

Example:

```
-------------- Transactions History --------------
Deposited : 500
Withdrawn : 200
Deposited : 1000
```

---

### 7. PIN Change

Users can change their ATM PIN by entering:

* Old PIN
* New PIN

The system verifies the old PIN before updating.

---

### 8. Account Blocking System

If a user enters the wrong PIN **three times**, the account status becomes:

```
blocked
```

Blocked accounts cannot log in again until manually reset.

---

# Project Structure

```
ATM-Simulator/
│
├── atm.py            # Main program file
├── database.json     # Stores account information
└── README.md         # Project documentation
```

---

# Program Architecture

The project follows an **Object-Oriented Design**.

### Classes Used

#### 1. `Account` Class

Handles all account operations.

Methods:

* `deposit()`
* `withdraw()`
* `checkBalance()`
* `showTransactions()`
* `changepin()`
* `HomePage()`

---

#### 2. `Atm` Class

Handles ATM system operations.

Methods:

* `login()`
* `create_account()`

---

# Data Storage

Account data is stored in a **JSON file**.

Example database structure:

```json
{
 "123456789": {
   "name": "Sukumar",
   "pin": 1234,
   "balance": 5000,
   "mobile": 9876543210,
   "transactions": [
     "Deposited : 500",
     "Withdrawn : 200"
   ],
   "status": "Active",
   "attempts": 3
 }
}
```

---

# Security Features

This project includes basic security mechanisms:

* Login attempt limit (3 attempts)
* Account blocking
* PIN verification
* Input validation for withdrawal and deposit amounts

---

# How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/SurendraMatsa/Python-mini-projects/tree/main/ATM%20Simulator
```

### 2. Navigate to project folder

```
cd atm-simulator-python
```

### 3. Run the program

```
python main.py
```

---

# Example Program Flow

```
----------- Welcome To MSB Bank -----------

1. Login
2. Create Account
```

If login is successful:

```
--------------- Main Menu ---------------

1. Deposit
2. Withdraw
3. Check Balance
4. Show Transactions
5. Change Pin
6. Exit
```

---
# Concepts Used

This project demonstrates the use of:

* Python OOP (Classes & Objects)
* JSON file handling
* Conditional logic
* Loops
* Error handling
* CLI application design

---

# Learning Outcome

Through this project, I learned:

* How to design a **real-world CLI application**
* Implement **authentication systems**
* Work with **persistent data storage**
* Apply **Object-Oriented Programming in Python**

---

# Author

**Surendra Matsa**

Python learner focused on building real-world projects and improving problem-solving skills.

---

