import sqlite3

# Connecting or Creating to the SQLite database
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# Table Creation
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY,
        book_name TEXT NOT NULL,
        author TEXT NOT NULL,
        price INTEGER NOT NULL
    )
''')

# Function to add a new book


def add_book(book_name, author, price):
    cursor.execute('INSERT INTO books (book_name, author, price) VALUES (?, ?, ?)',
                   (book_name, author, price))
    conn.commit()

# Function to retrieve all books


def get_all_books():
    cursor.execute('SELECT * FROM books')
    return cursor.fetchall()

# Function to retrieve a specific book by book_name


def get_book_by_book_name(book_name):
    cursor.execute('SELECT * FROM books WHERE book_name = ?', (book_name,))
    return cursor.fetchall()

# Function to update book information by book_name


def update_book_price(book_name, price):
    cursor.execute(
        'UPDATE books SET price = ? WHERE book_name = ?', (price, book_name))
    conn.commit()


# Function to delete a book by book_name
def delete_book(book_name):
    cursor.execute('DELETE FROM books WHERE book_name = ?', (book_name,))
    conn.commit()


# Testing add_book()
add_book('The Cruel Birth of Bangladesh', 'Archer K. Blood', 350)
add_book('The Blood Telegram: Nixon, Kissinger, and a Forgotten Genocide',
         ' Gary J. Bass', 900)


# Testing get_all_books()
print("All books:")
print(get_all_books())


# Testing get get_book_by_book_name()
print("Get Book(s) by Name")
print(get_book_by_book_name('The Cruel Birth of Bangladesh'))


# Testing get update_book_price()
print("Book Price Updating")
update_book_price(
    'The Blood Telegram: Nixon, Kissinger, and a Forgotten Genocide', 1200)


print("All books after update:")
print(get_all_books())


# Testing get delete_book()
print("Book Deleting")
delete_book('The Blood Telegram: Nixon, Kissinger, and a Forgotten Genocide')


print("All books after deletion:")
print(get_all_books())

# Close the connection
conn.close()
