import requests
from bs4 import BeautifulSoup
from config.config import BASE_URL
from services.database_service import save_data_to_db

def scraping():
    url = BASE_URL 
    database = {}
    x = 0
    global_counter = 0  # Initialize a global counter for unique keys
    while url:
        response = requests.get(url)
        print(f"Scraping {url}")
        soup = BeautifulSoup(response.text, "html.parser")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            s = soup.find('ol', class_='row')
            article_container = s.find_all('li')

            title = [article.find('article').find('h3').find('a').get('title') for article in article_container]
            price = [article.find('p', class_='price_color').get_text() for article in article_container]
            rating = [article.find('p', class_='star-rating')['class'][1] for article in article_container]
            image = [article.find('img')['src'] for article in article_container]
            availability = [article.find('p', class_='instock availability').get_text().strip() for article in article_container]
            for i in range(len(title)):
                database[global_counter] = {
                    "title": title[i],
                    "price": price[i],
                    "rating": rating[i],
                    "image": image[i],
                    "availability": availability[i]
                }
                global_counter += 1  # Increment the global counter for unique keys
        else:
            return f"Failed to fetch data: {response.status_code}"
        
        next_page = soup.find("a", text="next")  # Find 'Next' button
        # Update URL or stop
        if x>=1:
            url = BASE_URL + 'catalogue/' + next_page["href"] if next_page else None 
        else:
            url = BASE_URL + next_page["href"] if next_page else None 
        x+=1 
    return database
        