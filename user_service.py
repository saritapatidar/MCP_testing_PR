"""
user_service.py -- clean baseline version.

Push this file to your `development` branch first (as `user_service.py`).
Then create a `feature` branch off development, replace this file's
content with the "buggy" version, commit, and open a PR from
feature -> development. The AI reviewer should flag the issues
introduced in the buggy version.
"""

from __future__ import annotations

import hashlib
import logging
import secrets
import sqlite3
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

DB_PATH = "users.db"


@dataclass
class User:
    """A registered user."""

    username: str
    email: str
    tags: list[str] = field(default_factory=list)


def get_connection() -> sqlite3.Connection:
    """Open a connection to the users database."""
    return sqlite3.connect(DB_PATH)


def hash_password(password: str, salt: bytes | None = None) -> tuple[str, bytes]:
    """
    Hash a password with a random salt using PBKDF2.

    Args:
        password: Plaintext password to hash.
        salt: Optional salt to reuse (e.g. when verifying). A new
            random salt is generated if not provided.

    Returns:
        A tuple of (hex-encoded hash, salt bytes).
    """
    salt = salt or secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
    return digest.hex(), salt


def find_user_by_username(username: str) -> User | None:
    """
    Look up a user by username using a parameterized query.

    Args:
        username: Username to search for.

    Returns:
        The matching User, or None if not found.
    """
    connection = get_connection()
    try:
        cursor = connection.execute(
            "SELECT username, email FROM users WHERE username = ?",
            (username,),
        )
        row = cursor.fetchone()
    finally:
        connection.close()

    if row is None:
        return None

    return User(username=row[0], email=row[1])


def calculate_average_age(ages: list[int]) -> float:
    """
    Calculate the average of a list of ages.

    Args:
        ages: Ages to average. Must be non-empty.

    Returns:
        The average age.

    Raises:
        ValueError: If ages is empty.
    """
    if not ages:
        raise ValueError("Cannot calculate average of an empty list.")
    return sum(ages) / len(ages)


def read_config_lines(path: str) -> list[str]:
    """
    Read all non-empty lines from a config file.

    Args:
        path: Path to the config file.

    Returns:
        Non-empty, stripped lines from the file.
    """
    with open(path, encoding="utf-8") as config_file:
        return [line.strip() for line in config_file if line.strip()]


def add_tag(user: User, tag: str) -> None:
    """
    Add a tag to a user's tag list.

    Args:
        user: User to tag.
        tag: Tag to add.
    """
    user.tags.append(tag)


def safe_divide(numerator: float, denominator: float) -> float:
    """
    Divide two numbers, raising a clear error on division by zero.

    Args:
        numerator: The numerator.
        denominator: The denominator.

    Returns:
        numerator / denominator.

    Raises:
        ValueError: If denominator is zero.
    """
    if denominator == 0:
        raise ValueError("Cannot divide by zero.")
    return numerator / denominator


def process_login_attempts(usernames: list[str]) -> dict[str, int]:
    """
    Count login attempts per username.

    Args:
        usernames: A list of usernames, one entry per login attempt.

    Returns:
        A mapping of username to attempt count.
    """
    counts: dict[str, int] = {}
    for name in usernames:
        counts[name] = counts.get(name, 0) + 1
    return counts
