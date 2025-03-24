from scrapers.books_scraping import scraping
from services.database_service import create_table

def main():
    print("Setting up the database...")
    create_table()  # Ensure the database table exists

    print("Starting web scraping...")
    result = scraping()  # Scrape the data
    print(result)

    print("Scraping completed. Data saved to the database.")

if __name__ == "__main__":
    main()