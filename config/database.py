"""Database configuration and connection utilities."""

from __future__ import annotations

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "movies.db"


def get_connection() -> sqlite3.Connection:
    """Return a SQLite connection configured for the application.

    Returns:
        sqlite3.Connection: A connection object bound to the project database.

    Raises:
        RuntimeError: If the SQLite database cannot be opened.
    """
    try:
        connection = sqlite3.connect(DB_PATH)
        connection.row_factory = sqlite3.Row
        return connection
    except sqlite3.Error as exc:  # pragma: no cover - defensive guard
        raise RuntimeError(f"Unable to connect to database at {DB_PATH}.") from exc
