# Project Report

## 1. Problem Statement

Managing a personal movie collection manually becomes difficult as the collection grows. A movie enthusiast may want to store movie details, keep track of ratings, and understand patterns in a collection that spans various genres and release years.

Without a proper system, it is hard to:

- keep an organized record of movies
- quickly find the highest-rated films
- understand the average quality of the overall collection
- analyze the collection by genre

The Movie Collection Manager solves this problem by providing a simple and effective way to store movie records and retrieve meaningful summaries from them.

## 2. Features Implemented

The application includes the following core functionalities:

1. Add Movie
   - Collects Movie Name, Genre, Rating, and Release Year
   - Validates input data before saving

2. View Movies
   - Displays all stored movie records in a table

3. Average Rating
   - Calculates the average rating of the entire collection

4. Highest Rated Movie
   - Identifies the movie with the highest rating

5. Genre-wise Summary
   - Groups movies by genre and provides aggregated information

## 3. Database Design and Schema Breakdown

### Database Name
`movies.db`

### Table Name
`movies`

### Schema

```sql
CREATE TABLE IF NOT EXISTS movies (
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_name TEXT NOT NULL,
    genre TEXT NOT NULL,
    rating REAL NOT NULL CHECK (rating >= 0 AND rating <= 10),
    release_year INTEGER NOT NULL CHECK (release_year BETWEEN 1888 AND 2100)
);
```

### Column Breakdown

- `movie_id`: Unique primary key assigned to each movie record
- `movie_name`: Title of the movie
- `genre`: Genre classification such as Action, Comedy, Drama, Thriller, or Science Fiction
- `rating`: Numeric rating value between 0 and 10
- `release_year`: Release year of the movie

### Design Considerations

- `INTEGER PRIMARY KEY AUTOINCREMENT` is used for fast and reliable unique identification.
- `TEXT` is appropriate for movie names and genres.
- `REAL` is used for ratings to support decimal values.
- `CHECK` constraints ensure valid rating and year values.
- The schema is lightweight, easy to manage, and ideal for a personal collection database.

## 4. Setup Instructions

### Prerequisites

- Python 3.10 or later
- Windows PowerShell or Command Prompt
- Internet connection for installing Python packages

### Step 1: Open a Terminal

```powershell
cd d:\Movie_Collection_Manager
```

### Step 2: Create a Virtual Environment

```powershell
python -m venv .venv
```

### Step 3: Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell restricts script execution, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### Step 4: Upgrade pip and Install Requirements

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Run the Application

```powershell
streamlit run app.py
```

The application will open in the browser and display the Movie Collection Manager interface.

## 5. Screenshots

> Placeholder sections for required evidence screenshots.

### 5.1 Database Creation

Insert screenshot here showing `movies.db` successfully created.

### 5.2 Record Added Successfully

Insert screenshot here showing the movie addition flow and successful insert confirmation.

### 5.3 View Records Page

Insert screenshot here showing the collection table or grid with stored movies.

### 5.4 Summary Calculation

Insert screenshot here showing the Average Rating result.

### 5.5 Category / Genre Summary

Insert screenshot here showing the Genre-wise Summary output.

## 6. Prompts Used

The following prompt log records the major prompts used during development and iteration:

1. Prompt 1: Requirement generation for the Movie Collection Manager.
2. Prompt 2: Database design and SQLite schema creation.
3. Prompt 3: Application development using Streamlit and SQLite.
4. Prompt 4: Validation and analytics logic for average rating and highest-rated movie.
5. Prompt 5: Genre-wise summary generation.
6. Prompt 6: Code improvement for readability, refactoring, and testing.
7. Prompt 7: Unit test generation using pytest and mocking database behavior.
8. Prompt 8: Documentation refinement and final report preparation.

## 7. Testing Performed

The project was validated with the following checks:

### Functional Validation
- Verified database initialization
- Verified movie insertion into the `movies` table
- Verified movie retrieval from the collection
- Verified average rating calculation
- Verified highest rated movie logic
- Verified genre-wise summary aggregation

### Code Validation
- Python syntax compilation check
- Dependency installation verification
- Streamlit app startup validation

### Unit Testing
- Mocked database interactions using pytest
- Confirmed deterministic testing without a live SQLite file dependency
- Validated key query behaviors and summary calculations

## 8. Learning Outcomes

This project helped reinforce the following concepts:

- Python application structure and modular design
- Streamlit UI development
- SQLite database schema design and SQL querying
- Data validation and business logic implementation
- Parameterized SQL for security and reliability
- Test-driven validation using pytest and mocking
- Presentation of project documentation and technical reporting

## 9. Conclusion

The Movie Collection Manager is a complete, lightweight application that helps a movie enthusiast track and analyze a personal collection. It includes the core features required for storing movie records, viewing the collection, calculating averages, identifying top films, and summarizing data by genre.

The project is straightforward to set up, easy to extend, and demonstrates practical application of Python, Streamlit, and SQLite in a real-world use case.
