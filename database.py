import sqlite3

def initialize_database():
    conn = sqlite3.connect('book_reviews.db')
    cursor = conn.cursor()

    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            date_registered DATE NOT NULL,
            profile_picture TEXT
        );

        CREATE TABLE IF NOT EXISTS Books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT,
            description TEXT,
            year INTEGER,
            book_cover_image TEXT
        );

        CREATE TABLE IF NOT EXISTS FavouriteBook (
            user_id INTEGER,
            book_id INTEGER,
            PRIMARY KEY (user_id, book_id),
            FOREIGN KEY (user_id) REFERENCES Users (user_id),
            FOREIGN KEY (book_id) REFERENCES Books (book_id)
        );

        CREATE TABLE IF NOT EXISTS Reviews (
            review_id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            rating INTEGER NOT NULL,
            reviews_date DATE NOT NULL,
            user_id INTEGER,
            book_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES Users (user_id),
            FOREIGN KEY (book_id) REFERENCES Books (book_id)
        );
        ''')
    cursor.execute('DELETE FROM Books')
    cursor.execute('DELETE FROM sqlite_sequence WHERE name="Books"')

    books = [
        ("The Great Gatsby", "F. Scott Fitzgerald", "Romance",
         "Set amid the glamour of the Jazz Age, Jay Gatsby—with all the dark secrets of his past—tries to win back his love, Daisy Buchanan. Told from the perspective of her cousin Nick Carraway, this story is a brilliant blend of the American dream and moral decadence.",
         1925, "cover1.jpg"),

        ("1984", "George Orwell", "Fiction",
         "A dystopian masterpiece about totalitarianism, surveillance, and the struggle of one man to preserve his individuality in a bureaucratic world.",
         1949, "cover2.jpg"),

        ("To Kill a Mockingbird", "Harper Lee", "Romance",
         "Set in the Depression-era South, the novel follows Scout Finch, her brother Jem, and their father Atticus as they confront racism and injustice in their small town.",
         1960, "cover3.jpg"),

        ("Pride and Prejudice", "Jane Austen", "Romance",
         "A classic story following Elizabeth Bennet as she navigates manners, morality, and marriage in 19th-century England.",
         1813, "cover4.jpg"),

        ("Moby-Dick", "Herman Melville", "Classic",
         "Captain Ahab’s obsessive quest to take revenge on the white whale Moby Dick leads to tragedy and deep philosophical reflection.",
         1851, "cover5.jpg"),

        ("War and Peace", "Leo Tolstoy", "History",
         "An epic novel exploring Russian society during the Napoleonic Wars, blending personal drama with grand historical narrative.",
         1869, "cover6.jpg"),

        ("The Catcher in the Rye", "J. D. Salinger", "Fiction",
         "A coming-of-age story about teenage alienation and rebellion, told through the iconic voice of Holden Caulfield.",
         1951, "cover7.jpg"),

        ("The Hobbit", "J. R. R. Tolkien", "Fantasy",
         "Bilbo Baggins embarks on an unexpected adventure with a group of dwarves to reclaim treasure guarded by the mighty dragon Smaug.",
         1937, "cover8.jpg"),

        ("Brave New World", "Aldous Huxley", "Fiction",
         "A futuristic vision of a society obsessed with stability, technology, and consumerism, where individuality is sacrificed for control.",
         1932, "cover9.jpg"),

        ("Les Misérables", "Victor Hugo", "History",
         "A sweeping story of justice, redemption, and revolution in 19th-century France, centered on the life of ex-convict Jean Valjean.",
         1862, "cover10.jpg"),

        ("Crime and Punishment", "Fyodor Dostoevsky", "Psychology",
         "A psychological and philosophical exploration of morality and guilt through the mind of a man who commits murder.",
         1866, "cover11.jpg"),

        ("The Brothers Karamazov", "Fyodor Dostoevsky", "Psychology",
         "A profound exploration of faith, doubt, reason, and morality in the lives of three brothers torn by their father’s death.",
         1880, "cover12.jpg"),

        ("The Picture of Dorian Gray", "Oscar Wilde", "Classic",
         "A man trades his soul for eternal youth and beauty while his portrait ages, revealing the corruption of his spirit.",
         1890, "cover13.jpg"),

        ("Don Quixote", "Miguel de Cervantes", "Classic",
         "A comedic and tragic story of a man obsessed with chivalric ideals who sets out to revive knighthood.",
         1605, "cover14.jpg"),

        ("Jane Eyre", "Charlotte Brontë", "Romance",
         "The life story of an orphaned girl who grows into a strong, independent woman in Victorian England.",
         1847, "cover15.jpg"),

        ("Wuthering Heights", "Emily Brontë", "Comedy",
         "A dark tale of passion, revenge, and the destructive power of love set on the windswept moors of Yorkshire.",
         1847, "cover16.jpg"),

        ("Frankenstein", "Mary Shelley", "Horror",
         "A gothic novel about a scientist who creates life, only to be horrified by the consequences.",
         1818, "cover17.jpg"),

        ("Anna Karenina", "Leo Tolstoy", "Comedy",
         "A complex exploration of love, family, and social expectation in 19th-century Russia.",
         1877, "cover18.jpg"),

        ("The Divine Comedy", "Dante Alighieri", "Poetry",
         "An epic poem describing a journey through Hell, Purgatory, and Paradise in search of salvation.",
         1320, "cover19.jpg"),

        ("The Odyssey", "Homer", "Poetry",
         "An ancient Greek epic recounting Odysseus’s perilous journey home after the Trojan War.",
         -800, "cover20.jpg")
    ]

    cursor.executemany('''
           INSERT INTO Books (title, author, genre, description, year, book_cover_image)
           VALUES (?, ?, ?, ?, ?, ?)
       ''', books)

    print('Books added.')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    initialize_database()
    print('Database initialized.')