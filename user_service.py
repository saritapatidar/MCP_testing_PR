"""calculator.py -- clean baseline version. Push to development first."""


def divide(a: float, b: float) -> float:
    """Divide a by b, raising a clear error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def get_user_query(username: str) -> str:
    """Build a parameterized SQL query for a username lookup."""
    return "SELECT * FROM users WHERE username = ?"
