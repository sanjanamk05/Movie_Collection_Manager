"""Entry point for the Movie Collection Manager Streamlit app."""

from __future__ import annotations

from db.schema import initialize_database
from ui.dashboard import render_dashboard


def main() -> None:
    """Initialize the database and load the dashboard UI."""
    initialize_database()
    render_dashboard()


if __name__ == "__main__":
    main()
