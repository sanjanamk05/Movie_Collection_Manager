"""Validation helpers for movie input."""

from __future__ import annotations

from typing import Any


def validate_movie_input(movie_name: str, genre: str, rating: Any, release_year: Any) -> None:
    """Validate movie form inputs before insertion.

    Args:
        movie_name: The movie title.
        genre: The genre.
        rating: The movie rating.
        release_year: The release year.

    Raises:
        ValueError: When required input is invalid.
    """
    if not movie_name or not movie_name.strip():
        raise ValueError("Movie name is required.")

    if not genre or not genre.strip():
        raise ValueError("Genre is required.")

    try:
        rating_value = float(rating)
    except (TypeError, ValueError) as exc:
        raise ValueError("Rating must be a valid number.") from exc

    if not 0 <= rating_value <= 10:
        raise ValueError("Rating must be between 0 and 10.")

    try:
        year_value = int(release_year)
    except (TypeError, ValueError) as exc:
        raise ValueError("Release year must be a valid integer.") from exc

    if not 1888 <= year_value <= 2100:
        raise ValueError("Release year must be between 1888 and 2100.")
