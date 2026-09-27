"""Streamlit dashboard and interaction layer."""

from __future__ import annotations

from typing import Any

import pandas as pd
import streamlit as st

from services.analytics_service import (
    get_average_rating,
    get_genre_summary,
    get_highest_rated_movie,
)
from services.movie_service import create_movie, list_movies


def _safe_float(value: Any) -> float | None:
    """Convert a value to a float if possible; otherwise return None."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def render_movies_form() -> None:
    """Render the form used to add a new movie to the collection."""
    st.subheader("Add Movie")

    with st.form("movie_form", clear_on_submit=True):
        movie_name = st.text_input("Movie Name")
        genre = st.text_input("Genre")
        rating = st.number_input(
            "Rating",
            min_value=0.0,
            max_value=10.0,
            step=0.1,
            value=7.5,
        )
        release_year = st.number_input(
            "Release Year",
            min_value=1888,
            max_value=2100,
            step=1,
            value=2024,
        )

        submitted = st.form_submit_button("Add Movie")

        if submitted:
            try:
                create_movie(movie_name, genre, rating, release_year)
                st.success("Movie added successfully.")
            except ValueError as exc:
                st.error(str(exc))
            except RuntimeError as exc:
                st.error(f"Database error: {exc}")


def render_movies_table() -> None:
    """Render the current movie collection as a data table."""
    st.subheader("View Movies")

    try:
        movies = list_movies()
    except RuntimeError as exc:
        st.error(f"Unable to load movies: {exc}")
        return

    if not movies:
        st.info("No movies in the collection yet.")
        return

    df = pd.DataFrame(movies)
    st.dataframe(df, use_container_width=True, hide_index=True)


def render_summary_cards() -> None:
    """Render aggregate rating and collection summary metrics."""
    st.subheader("Collection Analytics")

    average_rating = get_average_rating()
    highest_movie = get_highest_rated_movie()
    genre_summary = get_genre_summary()

    col1, col2 = st.columns(2)

    with col1:
        if average_rating is None:
            st.metric("Average Rating", "N/A")
        else:
            st.metric("Average Rating", f"{average_rating:.2f}")

    with col2:
        if highest_movie is None:
            st.metric("Highest Rated Movie", "N/A")
        else:
            st.metric(
                "Highest Rated Movie",
                highest_movie["movie_name"],
                delta=f"{highest_movie['rating']:.1f} / 10",
            )

    st.markdown("### Genre-wise Summary")
    if not genre_summary:
        st.info("No genre summary available.")
        return

    genre_df = pd.DataFrame(genre_summary)
    genre_df = genre_df.rename(
        columns={
            "genre": "Genre",
            "movie_count": "Movie Count",
            "average_rating": "Average Rating",
        }
    )
    st.dataframe(genre_df, use_container_width=True, hide_index=True)


def render_dashboard() -> None:
    """Render the entire Movie Collection Manager dashboard."""
    st.set_page_config(page_title="Movie Collection Manager", layout="wide")
    st.title("Movie Collection Manager")
    st.caption("Track your movie collection, ratings, and genre insights.")

    render_movies_form()
    st.markdown("---")
    render_movies_table()
    st.markdown("---")
    render_summary_cards()
