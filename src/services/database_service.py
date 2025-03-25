import json
import sqlite3
import os

def create_table():
    os.makedirs("../data", exist_ok=True)  # Ensure the directory exists
    conn = sqlite3.connect("../data/books.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            price TEXT,
            rating TEXT,
            image TEXT,
            availability TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_data_to_db(data):
    conn = sqlite3.connect("../data/books.db")
    cursor = conn.cursor()
    for book in data.values():
        cursor.execute("""
            INSERT INTO books (title, price, rating, image, availability)
            VALUES (?, ?, ?, ?, ?)
        """, (book["title"], book["price"], book["rating"], book["image"], book["availability"]))
    conn.commit()
    conn.close()

def save_data_to_csv(data):
    os.makedirs("../data", exist_ok=True)  # Ensure the directory exists
    with open("../data/books.csv", "w") as file:
        file.write("title,price,rating,image,availability\n")
        for book in data.values():
            file.write(f"{book['title']},{book['price']},{book['rating']},{book['image']},{book['availability']}\n")

def save_data_to_json(data):
    os.makedirs("../data", exist_ok=True)  # Ensure the directory exists
    with open("../data/books.json", "w") as file:
        file.write(json.dumps(data, indent=4))