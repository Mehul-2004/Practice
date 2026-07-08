# Employee Management System

A console-based Employee Management System built with **Python** and **MySQL** that performs complete CRUD (Create, Read, Update, Delete) operations.

This project was built to practice modular programming, database integration, clean code principles, and software refactoring.

---

## Features

- Add Employee
- View All Employees
- Search Employees
- Update Employee Details
- Delete Employee
- Input Validation
- Modular Project Structure
- MySQL Database Integration

---

## Technologies Used

- Python 3
- MySQL
- mysql-connector-python
- Git
- GitHub

---

## Project Structure

```
employee_management_system/
│
├── database/
│   └── mysql_db.py
│
├── services/
│   └── employee_service.py
│
├── utils/
│   ├── formatter.py
│   ├── helper.py
│   ├── menu.py
│   └── validators.py
│
├── config.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
```

### Move into the project

```bash
cd employee_management_system
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure the database

Create a MySQL database named:

```
employee_management
```

Update your database credentials in `config.py`.

### Run the project

```bash
python main.py
```

---

## Learning Outcomes

During this project I learned:

- Python Functions
- Modular Programming
- CRUD Operations
- MySQL Integration
- Input Validation
- Code Refactoring
- Clean Project Structure
- Git & GitHub

---

## Future Improvements

- Export employees to CSV
- Dashboard with employee statistics
- Advanced search filters
- Logging
- Unit testing
- Environment variables
- Flask REST API
- Authentication

---

## Author

Mehul Ladwa