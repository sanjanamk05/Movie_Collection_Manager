# System Architecture Document

## 1. Overview

The Movie Collection Manager is a lightweight desktop-style web application built using Python, Streamlit, and SQLite. It is designed for a personal movie enthusiast who wants to store movie details, review the collection, and calculate collection insights such as average ratings, top-rated titles, and genre-wise summaries.

The architecture follows a simple three-layer design:

1. Presentation Layer (Streamlit UI)
2. Application Layer (Python business logic)
3. Data Layer (SQLite database)

This structure ensures low complexity, easy maintainability, and clear separation of concerns while allowing room for future extensions such as filtering, sorting, editing, and analytics.

---

## 2. Technology Stack

- Python 3.x
- Streamlit
- SQLite
- Standard Python modules
- Git for version control

---

## 3. Architecture Principles

The system is designed around the following principles:

- Simplicity: Minimal dependencies and a straightforward data model.
- Modularity: Separation of UI, database logic, and helper functions.
- Reliability: Validated inputs and consistent database schema.
- Performance: Optimized SQLite schema for fast reads and efficient storage.
- Maintainability: Clear folder structure and reusable modules.

---

## 4. High-Level Architecture

### 4.1 Components

#### Presentation Layer
- Streamlit interface for movie entry and data display
- Forms for Add Movie
- Views for listing collection records
- Summary panels showing average rating, top movie, and genre overview

#### Application Layer
- Data validation logic
- Database connection and query handling
- Aggregation functions for analytics
- Business logic for summary generation

#### Data Layer
- SQLite database file: `movies.db`
- Single table: `movies`
- Persistent record storage for all movie entries

### 4.2 Interaction Model

User actions trigger Streamlit events, which call Python functions. Those functions connect to SQLite, execute DML/queries, and return results for display in the interface.

---

## 5. Database Design

### 5.1 Database Name
`movies.db`

### 5.2 Table Name
`movies`

### 5.3 Schema

The core table stores each movie record with essential metadata:

- `movie_id`: unique identifier
- `movie_name`: movie title
- `genre`: movie category or type
- `rating`: numerical rating value
- `release_year`: release year of the movie

### 5.4 Recommended DDL

```sql
CREATE TABLE IF NOT EXISTS movies (
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_name TEXT NOT NULL,
    genre TEXT NOT NULL,
    rating REAL NOT NULL CHECK (rating >= 0 AND rating <= 10),
    release_year INTEGER NOT NULL CHECK (release_year BETWEEN 1888 AND 2100)
);
```

### 5.5 Rationale for Data Types

- `INTEGER PRIMARY KEY AUTOINCREMENT`: Efficient primary key for unique row identification.
- `TEXT NOT NULL`: Best choice for movie names and genres since values are string-based and human-readable.
- `REAL NOT NULL`: Appropriate for ratings because they may include decimals and support numeric analysis.
- `INTEGER NOT NULL`: Suitable for release_year and efficient for filtering or grouping by year.
- `CHECK` constraints: Prevent invalid data such as negative ratings or impossible release years.

### 5.6 Indexing Strategy

For a modest dataset, the basic schema is efficient; however, for faster retrieval, indexing can be added on commonly queried fields:

```sql
CREATE INDEX IF NOT EXISTS idx_movies_genre ON movies (genre);
CREATE INDEX IF NOT EXISTS idx_movies_rating ON movies (rating DESC);
CREATE INDEX IF NOT EXISTS idx_movies_release_year ON movies (release_year);
```

### 5.7 Example Insert Query

```sql
INSERT INTO movies (movie_name, genre, rating, release_year)
VALUES ('Inception', 'Science Fiction', 8.8, 2010);
```

### 5.8 Example Analytical Queries

#### Average Rating
```sql
SELECT AVG(rating) AS average_rating
FROM movies;
```

#### Highest Rated Movie
```sql
SELECT movie_name, genre, rating, release_year
FROM movies
ORDER BY rating DESC, movie_id ASC
LIMIT 1;
```

#### Genre-wise Summary
```sql
SELECT genre,
       COUNT(*) AS movie_count,
       AVG(rating) AS avg_genre_rating
FROM movies
GROUP BY genre
ORDER BY movie_count DESC, genre ASC;
```

---

## 6. Database Access Model

The application will use a lightweight database layer that handles:

- Connection creation to `movies.db`
- Schema initialization
- CRUD operations
- Aggregated summary queries
- Error handling for database exceptions

This layer keeps database logic separate from the Streamlit interface and supports easier testing and future expansion.

---

## 7. Project Folder Structure

A production-ready folder structure for modularity is recommended as follows:

```text
Movie_Collection_Manager/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── movies.db
│
├── config/
│   ├── __init__.py
│   └── database.py
│
├── db/
│   ├── __init__.py
│   ├── schema.py
│   └── queries.py
│
├── ui/
│   ├── __init__.py
│   ├── dashboard.py
│   ├── forms.py
│   └── summary.py
│
├── services/
│   ├── __init__.py
│   ├── movie_service.py
│   └── analytics_service.py
│
├── utils/
│   ├── __init__.py
│   ├── validation.py
│   └── helpers.py
│
├── tests/
│   ├── __init__.py
│   ├── test_database.py
│   └── test_analytics.py
│
└── assets/
    └── screenshots/
```

### 7.1 Module Responsibilities

#### `config/database.py`
- Contains database connection configuration
- Creates SQLite connection object
- Initializes database path

#### `db/schema.py`
- Contains DDL definitions
- Ensures schema exists before use

#### `db/queries.py`
- Encapsulates SQL queries for CRUD and analytics
- Keeps logic centralized and reusable

#### `ui/forms.py`
- Contains Streamlit form components for Add Movie and input capture

#### `ui/dashboard.py`
- Defines the main app dashboard layout
- Displays collection records and summary cards

#### `ui/summary.py`
- Displays average rating, highest-rated movie, and genre summary results

#### `services/movie_service.py`
- Handles create, read, and aggregate operations
- Coordinates between UI and database layers

#### `services/analytics_service.py`
- Implements calculations like average rating and genre summary

#### `utils/validation.py`
- Validates required inputs, numeric ratings, and year values

#### `utils/helpers.py`
- Common helper functions such as formatting results or null handling

---

## 8. Application Flow

### 8.1 Add Movie Flow
1. User opens the Streamlit app.
2. User enters movie details in a form.
3. The frontend validates the fields.
4. Python service layer sends insert request to SQLite.
5. The database stores the record.
6. Success message appears and the collection refreshes.

### 8.2 View Collection Flow
1. User navigates to the collection view.
2. Query is executed against `movies` table.
3. Results are fetched and displayed in a table.
4. Data is refreshed when new records are added.

### 8.3 Summary Flow
1. User requests average rating or highest-rated movie.
2. Service layer calls summary queries.
3. SQLite computes results.
4. Results are returned to the UI and displayed on dashboard cards.

---

## 9. Data Flow Diagram (Text Representation)

```text
+-----------------------+
|       User             |
|   (Movie Collector)    |
+----------+------------+
           |
           | 1. Enters movie details
           v
+-----------------------+
| Streamlit UI           |
| - Add Movie Form      |
| - Movie List View     |
| - Summary Dashboard   |
+----------+------------+
           |
           | 2. Calls Python functions
           v
+-----------------------+
| Application Layer      |
| - Validation          |
| - Business Logic      |
| - Query Execution     |
+----------+------------+
           |
           | 3. SQL queries / inserts
           v
+-----------------------+
| SQLite Database        |
| movies.db             |
| Table: movies         |
| movie_id              |
| movie_name            |
| genre                 |
| rating                |
| release_year          |
+----------+------------+
           |
           | 4. Returns results
           v
+-----------------------+
| Streamlit UI          |
| Displays collection, |
| ratings, and summary  |
+-----------------------+
```

---

## 10. Scalability and Future Architecture Considerations

Although the current system is intentionally simple, the architecture supports future improvement without major redesign.

### Possible future enhancements
- Add search and filter functionality
- Support edit and delete operations
- Add favorites/watchlist indicators
- Generate charts and visual dashboards
- Import/export data in CSV or JSON
- Add user authentication for multi-user access

These enhancements can be layered into the same architecture by extending the service layer and UI components without changing the database model drastically.

---

## 11. Security and Data Integrity Considerations

- Use validation before writing to the database.
- Restrict data types and ranges with SQL constraints.
- Ensure database connection is created once and reused for efficiency.
- Handle exceptions gracefully to avoid app crashes.
- Keep the database file in a controlled location and avoid storing sensitive data in plaintext outside the app context.

---

## 12. Summary

The Movie Collection Manager architecture is intentionally minimal but robust. It uses a clean separation between UI, business logic, and database layers. SQLite is the ideal choice for this project because it is lightweight, easy to manage, and well-suited to local personal data storage. The schema and folder structure support a stable MVP while leaving room for future enhancements in functionality and analytics.
