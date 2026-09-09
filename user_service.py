"""calculator.py -- buggy version. Replace on a feature branch, then PR to development."""


def divide(a: float, b: float) -> float:
    """Divide a by b."""
    return a / b


def get_user_query(username: str) -> str:
    """Build a SQL query for a username lookup."""
    return f"SELECT * FROM users WHERE username = '{username}'"
