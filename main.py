from pymongo import MongoClient
from scrape import scrape_tenders

# Connect to the MongoDB database
client = MongoClient('localhost', 27017)
db = client['tenders_database']
collection = db['tenders_collection']


def save_to_mongo(data):
    try:
        collection.insert_many(data)
        print("Data saved to MongoDB")
    except Exception as e:
        print(f"An error occurred: {e}")


# website to scrape

website = ("https://www.tenders.go.ke")


## 1. scraping the data from the web

try:
    tend_table = scrape_tenders(website)
    database = save_to_mongo(tend_table)
except Exception as e:
    print(f"An error occurred: You might want to check your internet connection then try again {e}")


 


   






