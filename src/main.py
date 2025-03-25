from scrapers.books_scraping import scraping
from services.database_service import create_table
from services.database_service import save_data_to_csv
from services.database_service import save_data_to_json
from services.database_service import save_data_to_db

def main():
    print("Welcome to the web scraping app! Datas are being scraped from the website 'http://books.toscrape.com/'\n")
    choice = input("How do you want to save the data? Press Enter to save to the database, or type 'csv' or 'json' to save to a file: ")

    print("Starting web scraping...")
    result = scraping()  # Scrape the data

    if choice == 'csv':
        save_data_to_csv(result) # Save the data to a CSV file
    elif choice == 'json':
        save_data_to_json(result)  # Save the data to a JSON file
    else:
        print("Setting up the database...")
        create_table()  # Ensure the database table exists
        save_data_to_db(result)  # Save the data to the database
    

    print("\nScraping completed. Data saved to the database.")

if __name__ == "__main__":
    main()