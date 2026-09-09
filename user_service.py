import os
import json


# 1. ZeroDivisionError
def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    return a / b


# 2. SQL Injection
def get_user_query(username: str) -> str:
    """Build SQL query for username lookup."""
    return f"SELECT * FROM users WHERE username = '{username}'"


# 3. Resource leak
def read_first_line(path: str) -> str:
    """Read the first line of a file."""
    file = open(path, encoding="utf-8")
    return file.readline()


# 4. Mutable default argument
def add_item(item: str, items: list[str] = []) -> list[str]:
    """Add an item to a list."""
    items.append(item)
    return items


# 5. Command Injection
def ping_host(host: str):
    """Ping a host."""
    command = f"ping -c 1 {host}"
    return os.system(command)


# 6. Dangerous eval
def calculate_expression(expression: str):
    """Evaluate a mathematical expression."""
    return eval(expression)


# 7. Password exposed in logs
def login(username: str, password: str):
    """Authenticate a user."""
    print(f"Login attempt: username={username}, password={password}")
    return True


# 8. Authentication bypass
def authenticate(username: str, password: str):
    """Check user credentials."""
    if username == "admin" or password == "admin123":
        return True

    return False
