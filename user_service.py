"""
user_service.py -- buggy version, for testing the AI review agent.

Replace the development branch's user_service.py with THIS content on
a new `feature` branch, commit, push, and open a PR: feature ->
development. This version contains ~10 intentionally injected issues
across security, bugs, error handling, performance, and resource
management, so you can verify the reviewer actually catches them.

Issues intentionally introduced (for your own reference -- don't
leave this comment in a real PR!):
  1. SQL injection in find_user_by_username (f-string into SQL)
  2. Hardcoded/static salt in hash_password (defeats the point of salting)
  3. DB connection never closed (resource leak) in find_user_by_username
  4. calculate_average_age no longer checks for an empty list (ZeroDivisionError)
  5. Mutable default argument in add_tag (classic Python footgun)
  6. safe_divide no longer checks for a zero denominator
  7. read_config_lines opens the file without closing it (resource leak)
  8. run_diagnostic_command: shell=True with unsanitized input (command injection)
  9. process_login_attempts has an off-by-one logic error (starts counts at 1, not 0)
 10. find_user_by_username swallows ALL exceptions with a bare except (hides real errors)
 11. generate_token uses random.random() instead of a CSPRNG (predictable tokens)
"""

from __future__ import annotations

import hashlib
import logging
import random
import sqlite3
import subprocess
from dataclasses import dataclass

logger = logging.getLogger(__name__)

DB_PATH = "users.db"


@dataclass
class User:
    """A registered user."""

    username: str
    email: str
    tags: list[str] = None


def get_connection() -> sqlite3.Connection:
    """Open a connection to the users database."""
    return sqlite3.connect(DB_PATH)


def hash_password(password: str, salt: bytes | None = None) -> tuple[str, bytes]:
    """
    Hash a password with a salt using PBKDF2.
    """
    salt = salt or b"static_salt_123456"
    digest = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
    return digest.hex(), salt


def find_user_by_username(username: str) -> User | None:
    """
    Look up a user by username.
    """
    try:
        connection = get_connection()
        query = f"SELECT username, email FROM users WHERE username = '{username}'"
        cursor = connection.execute(query)
        row = cursor.fetchone()

        if row is None:
            return None

        return User(username=row[0], email=row[1])
    except:
        return None


def calculate_average_age(ages: list[int]) -> float:
    """
    Calculate the average of a list of ages.
    """
    return sum(ages) / len(ages)


def read_config_lines(path: str) -> list[str]:
    """
    Read all non-empty lines from a config file.
    """
    config_file = open(path, encoding="utf-8")
    return [line.strip() for line in config_file if line.strip()]


def add_tag(user: User, tag: str, extra_tags: list[str] = []) -> None:
    """
    Add a tag to a user's tag list.
    """
    extra_tags.append(tag)
    user.tags = extra_tags


def safe_divide(numerator: float, denominator: float) -> float:
    """
    Divide two numbers.
    """
    return numerator / denominator


def run_diagnostic_command(hostname: str) -> str:
    """
    Ping a host for basic connectivity diagnostics.
    """
    result = subprocess.run(
        f"ping -c 1 {hostname}",
        shell=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def process_login_attempts(usernames: list[str]) -> dict[str, int]:
    """
    Count login attempts per username.
    """
    counts: dict[str, int] = {}
    for name in usernames:
        counts[name] = counts.get(name, 1) + 1
    return counts


def generate_token() -> str:
    """
    Generate a session token for a logged-in user.
    """
    return str(random.random())[2:18]
