"""Schema initialization for the movie collection database."""

from __future__ import annotations

import sqlite3

from config.database import get_connection


def initialize_database() -> None:
    """Ensure the required database schema exists.

    Creates the ``movies`` table when it does not already exist.
    """
    connection: sqlite3.Connection | None = None
    try:
        connection = get_connection()
        with connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS movies (
                    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    movie_name TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    rating REAL NOT NULL CHECK (rating >= 0 AND rating <= 10),
                    release_year INTEGER NOT NULL CHECK (release_year BETWEEN 1888 AND 2100)
                )
                """
            )
    except sqlite3.Error as exc:
        raise RuntimeError("Failed to initialize the database schema.") from exc
    finally:
        if connection is not None:
            connection.close()
