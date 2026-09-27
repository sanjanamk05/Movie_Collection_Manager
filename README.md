# Movie Collection Manager

## 1. Problem Statement and Features Implemented

The Movie Collection Manager is a simple application created for a movie enthusiast who wants to maintain a personal library of films across multiple genres. As the collection grows, manually tracking details such as movie names, release years, ratings, and genre distribution becomes difficult.

The application addresses this by allowing the user to:

- add movie records
- view all stored movies
- calculate the average rating of the collection
- identify the highest-rated movie
- generate a genre-wise summary

## 2. Features Implemented

- Add Movie with Name, Genre, Rating, and Release Year
- View Movies in a tabular format
- Average Rating calculation
- Highest Rated Movie detection
- Genre-wise Summary aggregation

## 3. Technology Stack

- Python
- Streamlit
- SQLite
- pytest (for unit testing)

## 4. Database Design and Schema Breakdown

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

- `movie_id`: unique identifier
- `movie_name`: title of the movie
- `genre`: category such as Action, Comedy, Drama, or Science Fiction
- `rating`: numeric rating in the range 0 to 10
- `release_year`: year of movie release

## 5. Setup Instructions

### Create a Virtual Environment

```powershell
cd d:\Movie_Collection_Manager
python -m venv .venv
```

### Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks execution, run the following once:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Run the Application

```powershell
streamlit run app.py
```

The application will run in the browser at:

```text
http://localhost:8501
```

## 6. Project Structure

```text
Movie_Collection_Manager/
├── app.py
├── requirements.txt
├── README.md
├── Project_Report.md
├── movies.db
├── config/
├── db/
├── services/
├── ui/
├── utils/
├── tests/
├── .gitignore
└── assets/
```

## 7. Screenshots

> Placeholder sections for required screenshot evidence.

### Database Creation

Insert screenshot here showing the SQLite database file created successfully.

### Record Added Successfully

Insert screenshot here showing user input and success confirmation after insertion.

### View Records

Insert screenshot here showing the list or table of movie records.

### Summary Calculation

Insert screenshot here showing the average rating summary calculation.

### Category Summary

Insert screenshot here showing the genre-wise summary output.

## 8. Prompts Used

1. Prompt 1: Requirement generation for the Movie Collection Manager.
2. Prompt 2: SQLite schema and database design.
3. Prompt 3: Streamlit UI and form development.
4. Prompt 4: Add database query and analytics logic.
5. Prompt 5: Genre summary and report refinement.
6. Prompt 6: Code refactoring and testing improvements.
7. Prompt 7: Pytest unit test generation with mocked database connection.
8. Prompt 8: Documentation generation and final project report writing.

## 9. Testing Performed

### Functional Testing
- Database initialization check
- Add movie record validation
- View records verification
- Average rating calculation validation
- Highest rated movie validation
- Genre summary validation

### Unit Testing
- Mocked database connection testing using pytest
- Validation of deterministic query behavior
- Verification of summary logic without a live SQLite file

### Code Validation
- Dependency installation check
- Python syntax/compile check
- Streamlit startup check

## 10. Notes

The database schema is created automatically when the app launches, and the application is designed to be simple, modular, and easy to extend for future requirements such as editing, filtering, or export features.
