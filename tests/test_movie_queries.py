"""Unit tests for movie database insertion and summary calculations."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from db import queries


@pytest.fixture
def mock_connection() -> MagicMock:
    """Return a mock SQLite connection with deterministic query results."""
    connection = MagicMock()
    cursor = MagicMock()
    connection.execute.return_value = cursor
    return connection


def test_add_movie_inserts_record_with_parameterized_sql(mock_connection: MagicMock) -> None:
    """Ensure add_movie executes a parameterized insert and returns the last row id."""
    mock_connection.execute.return_value.lastrowid = 7

    with patch("db.queries.get_connection", return_value=mock_connection):
        result = queries.add_movie("Inception", "Science Fiction", 8.8, 2010)

    assert result == 7
    mock_connection.execute.assert_called_once()
    sql = mock_connection.execute.call_args.args[0]
    params = mock_connection.execute.call_args.args[1]

    assert "INSERT INTO movies" in sql
    assert params == ("Inception", "Science Fiction", 8.8, 2010)
    mock_connection.close.assert_called_once()


def test_fetch_average_rating_returns_mean_value(mock_connection: MagicMock) -> None:
    """Ensure average rating queries return the expected numeric result."""
    mock_connection.execute.return_value.fetchone.return_value = {"average_rating": 8.75}

    with patch("db.queries.get_connection", return_value=mock_connection):
        result = queries.fetch_average_rating()

    assert result == 8.75
    mock_connection.close.assert_called_once()


def test_fetch_highest_rated_movie_returns_top_record(mock_connection: MagicMock) -> None:
    """Ensure the highest-rated movie query returns the top movie entry."""
    mock_connection.execute.return_value.fetchone.return_value = {
        "movie_id": 2,
        "movie_name": "The Dark Knight",
        "genre": "Action",
        "rating": 9.0,
        "release_year": 2008,
    }

    with patch("db.queries.get_connection", return_value=mock_connection):
        result = queries.fetch_highest_rated_movie()

    assert result == {
        "movie_id": 2,
        "movie_name": "The Dark Knight",
        "genre": "Action",
        "rating": 9.0,
        "release_year": 2008,
    }
    mock_connection.close.assert_called_once()


def test_fetch_genre_summary_returns_grouped_statistics(mock_connection: MagicMock) -> None:
    """Ensure genre summary aggregation returns expected count and ratings by genre."""
    mock_connection.execute.return_value.fetchall.return_value = [
        SimpleNamespace(genre="Action", movie_count=2, average_rating=8.9),
        SimpleNamespace(genre="Comedy", movie_count=1, average_rating=8.5),
    ]

    with patch("db.queries.get_connection", return_value=mock_connection):
        result = queries.fetch_genre_summary()

    assert result == [
        {"genre": "Action", "movie_count": 2, "average_rating": 8.9},
        {"genre": "Comedy", "movie_count": 1, "average_rating": 8.5},
    ]
    mock_connection.close.assert_called_once()


def test_fetch_movie_records_handles_empty_result(mock_connection: MagicMock) -> None:
    """Ensure a no-result query returns an empty list without errors."""
    mock_connection.execute.return_value.fetchall.return_value = []

    with patch("db.queries.get_connection", return_value=mock_connection):
        result = queries.fetch_movies()

    assert result == []
    mock_connection.close.assert_called_once()
