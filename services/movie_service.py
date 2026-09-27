"""Service layer for movie CRUD operations."""

from __future__ import annotations

from typing import Any

from db.queries import add_movie, fetch_movies
from utils.validation import validate_movie_input


def create_movie(movie_name: str, genre: str, rating: Any, release_year: Any) -> int:
    """Validate and insert a new movie record.

    Args:
        movie_name: Movie title.
        genre: Genre classification.
        rating: Numeric rating value.
        release_year: Release year.

    Returns:
        int: The inserted movie identifier.
    """
    validate_movie_input(movie_name, genre, rating, release_year)
    return add_movie(
        movie_name=movie_name.strip(),
        genre=genre.strip(),
        rating=float(rating),
        release_year=int(release_year),
    )


def list_movies() -> list[dict[str, Any]]:
    """Return all movies currently stored in the database."""
    return fetch_movies()
