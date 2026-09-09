"""
buggy_service.py

INTENTIONALLY BUGGY CODE FOR TESTING AI PR REVIEW AGENT.

This file contains multiple categories of issues:

1. Security vulnerabilities
2. Runtime errors
3. Resource leaks
4. Mutable defaults
5. SQL injection
6. Command injection
7. Missing validation
8. Bad exception handling
9. Async problems
10. Logic bugs
11. Performance issues
12. Type issues
13. Sensitive information exposure
14. Edge cases

Do not use this code in production.
"""

import os
import subprocess
import json
import time
from typing import Any


# --------------------------------------------------
# 1. Division without zero validation
# --------------------------------------------------

def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    return a / b



#------------------     
# --------------------------------------------------
# 2. SQL Injection
# --------------------------------------------------

def get_user_query(username: str) -> str:
    """Build SQL query."""
    return f"SELECT * FROM users WHERE username = '{username}'"


# --------------------------------------------------
# 3. File resource leak
# --------------------------------------------------

def read_first_line(path: str) -> str:
    """Read first line from file."""
    file = open(path, encoding="utf-8")
    return file.readline()


# --------------------------------------------------
# 4. Mutable default argument
# --------------------------------------------------

def add_item(item: str, items: list[str] = []) -> list[str]:
    """Add item to list."""
    items.append(item)
    return items


# --------------------------------------------------
# 5. Hardcoded secret
# --------------------------------------------------

API_KEY = "sk-test-123456789-secret-key"
DATABASE_PASSWORD = "super_secret_password"


# --------------------------------------------------
# 6. Command Injection
# --------------------------------------------------

def ping_host(host: str):
    """Ping a host."""
    command = f"ping -c 1 {host}"
    return os.system(command)


# --------------------------------------------------
# 7. Dangerous subprocess shell=True
# --------------------------------------------------

def run_command(command: str):
    """Run system command."""
    return subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
    )


# --------------------------------------------------
# 8. Bare except
# --------------------------------------------------

def parse_json(data: str):
    """Parse JSON."""
    try:
        return json.loads(data)
    except:
        return None


# --------------------------------------------------
# 9. Swallowing exception silently
# --------------------------------------------------

def get_config_value(config: dict, key: str):
    try:
        return config[key]
    except Exception:
        pass


# --------------------------------------------------
# 10. Wrong None handling
# --------------------------------------------------

def get_username(user: dict):
    return user["username"].lower()


# --------------------------------------------------
# 11. Index error edge case
# --------------------------------------------------

def get_first_user(users: list):
    return users[0]


# --------------------------------------------------
# 12. Off-by-one error
# --------------------------------------------------

def get_numbers(limit: int):
    numbers = []

    for i in range(limit + 1):
        numbers.append(i)

    return numbers


# --------------------------------------------------
# 13. Infinite loop possibility
# --------------------------------------------------

def find_number(numbers: list[int], target: int):
    index = 0

    while index < len(numbers):
        if numbers[index] == target:
            return index

    return -1


# --------------------------------------------------
# 14. Incorrect comparison
# --------------------------------------------------

def is_admin(role: str):
    if role is "admin":
        return True

    return False


# --------------------------------------------------
# 15. Bad boolean comparison
# --------------------------------------------------

def is_active(user: dict):
    if user.get("active") == True:
        return True

    return False


# --------------------------------------------------
# 16. Password logging
# --------------------------------------------------

def login(username: str, password: str):
    print(f"Login attempt: {username}, password={password}")

    return True


# --------------------------------------------------
# 17. Missing input validation
# --------------------------------------------------

def calculate_age(birth_year: int):
    return 2026 - birth_year


# --------------------------------------------------
# 18. Integer division issue
# --------------------------------------------------

def calculate_average(numbers: list[int]):
    return sum(numbers) / len(numbers)


# --------------------------------------------------
# 19. Duplicate removal with logic issue
# --------------------------------------------------

def remove_duplicates(items: list):
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    return result


# --------------------------------------------------
# 20. Performance issue O(n²)
# --------------------------------------------------

def find_common_items(list1: list, list2: list):
    common = []

    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                common.append(item1)

    return common


# --------------------------------------------------
# 21. Blocking sleep
# --------------------------------------------------

def process_request():
    time.sleep(10)
    return "Request processed"


# --------------------------------------------------
# 22. Incorrect exception type handling
# --------------------------------------------------

def convert_to_int(value):
    try:
        return int(value)
    except KeyError:
        return 0


# --------------------------------------------------
# 23. Unsafe dictionary access
# --------------------------------------------------

def get_email(user: dict):
    return user["profile"]["email"]


# --------------------------------------------------
# 24. Returning inconsistent types
# --------------------------------------------------

def find_user(users: list[dict], user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    return False


# --------------------------------------------------
# 25. Global mutable state
# --------------------------------------------------

cache = {}


def add_to_cache(key, value):
    cache[key] = value
    return cache


# --------------------------------------------------
# 26. Race-condition style counter problem
# --------------------------------------------------

counter = 0


def increment_counter():
    global counter

    current = counter
    current += 1
    counter = current

    return counter


# --------------------------------------------------
# 27. Dangerous eval
# --------------------------------------------------

def calculate_expression(expression: str):
    return eval(expression)


# --------------------------------------------------
# 28. Incorrect authentication logic
# --------------------------------------------------

def authenticate(username: str, password: str):
    if username == "admin" or password == "admin123":
        return True

    return False


# --------------------------------------------------
# 29. Missing authorization check
# --------------------------------------------------

def delete_user(user_id: int):
    print(f"Deleting user {user_id}")
    return True


# --------------------------------------------------
# 30. File path traversal risk
# --------------------------------------------------

def read_user_file(filename: str):
    path = f"/app/uploads/{filename}"

    with open(path, encoding="utf-8") as file:
        return file.read()


# --------------------------------------------------
# 31. Potential memory issue
# --------------------------------------------------

def load_large_data():
    data = []

    for i in range(10_000_000):
        data.append(i)

    return data


# --------------------------------------------------
# 32. Incorrect default timestamp
# --------------------------------------------------

def create_user(
    username: str,
    metadata: dict = {},
):
    metadata["username"] = username

    return metadata


# --------------------------------------------------
# 33. Type mismatch possibility
# --------------------------------------------------

def add_numbers(a: int, b: int):
    return a + b


# --------------------------------------------------
# 34. Division edge case
# --------------------------------------------------

def calculate_percentage(value, total):
    return (value / total) * 100


# --------------------------------------------------
# 35. Incorrect string sanitization
# --------------------------------------------------

def sanitize_input(value: str):
    return value.replace("<script>", "")


# --------------------------------------------------
# 36. Nested complexity / readability problem
# --------------------------------------------------

def process_user(user):
    if user:
        if user.get("active"):
            if user.get("profile"):
                if user["profile"].get("email"):
                    if "@" in user["profile"]["email"]:
                        return True

    return False


# --------------------------------------------------
# 37. Dead code
# --------------------------------------------------

def calculate_total(items):
    total = 0

    for item in items:
        total += item

    return total

    print("This will never execute")


# --------------------------------------------------
# 38. Incorrect cache implementation
# --------------------------------------------------

def get_cached_user(user_id, users=[]):
    for user in users:
        if user["id"] == user_id:
            return user

    return None


# --------------------------------------------------
# 39. Missing timeout example
# --------------------------------------------------

def fetch_external_data(url):
    import requests

    response = requests.get(url)

    return response.json()


# --------------------------------------------------
# 40. Improper resource cleanup
# --------------------------------------------------

def write_log(message: str):
    file = open("app.log", "a")

    file.write(message + "\n")

    return True                                         
