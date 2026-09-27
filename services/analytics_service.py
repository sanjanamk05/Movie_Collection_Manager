"""Service layer for movie analytics and summaries."""

from __future__ import annotations

from typing import Any

from db.queries import (
    fetch_average_rating,
    fetch_genre_summary,
    fetch_highest_rated_movie,
)


def get_average_rating() -> float | None:
    """Return the collection-wide average movie rating."""
    return fetch_average_rating()


def get_highest_rated_movie() -> dict[str, Any] | None:
    """Return the highest rated movie in the collection."""
    return fetch_highest_rated_movie()


def get_genre_summary() -> list[dict[str, Any]]:
    """Return a summary of movie counts and average ratings by genre."""
    return fetch_genre_summary()
