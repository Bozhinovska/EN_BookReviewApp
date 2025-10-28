# EN Book Review Flask App

This project is an **updated version of the original Book Review Application**, which was created in my native language.  
The current version is **fully translated into English**, including all interface elements, database content, and book descriptions.  

It’s a Flask-based web application that allows users to browse, review, and favourite books.  
The app uses **SQLite** as a local database and comes with preloaded book data.

---

## How to Run the Project

### Clone the repository
```bash
git clone https://github.com/Bozhinovska/EN_BookReviewApp.git
````
```bash
cd EN_BookReviewApp
````

```bash
pip install Flask
```

### Initialize the database

Before running the Flask app, create and populate the database:

```bash
python3 database.py
```

This will create `book_reviews.db` and all necessary tables.

### Run the Flask application

```bash
python3 app.py
```

### Open your browser

Go to:

```
http://127.0.0.1:5000
```

---

## Project Structure

```
EN_BookReviewApp/
│
├── app.py              # Main Flask application
├── database.py         # Initializes and populates the database
├── book_reviews.db     # SQLite database (created after initialization)
├── templates/          # HTML templates
├── static/             # CSS, JS, and images
├── .idea/              # PyCharm project files
├── __pycache__/        # Python cache files
├── .DS_Store           # macOS system file
└── README.md           # Project documentation
```

---

## Notes

* Run `database.py` **only the first time** to initialize your database.
* Afterwards, just run `app.py` to start the app.
* Default Flask port is **5000**, so the app is accessible at:
[http://127.0.0.1:5000](http://127.0.0.1:5000)


```
