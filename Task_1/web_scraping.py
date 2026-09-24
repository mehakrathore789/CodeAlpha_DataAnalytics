import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

data = []

# Scrape all 50 pages
for page in range(1, 51):

    url = base_url.format(page)

    print(f"Scraping page {page}...")

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print(f"Failed to fetch page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        # Book title
        title = book.h3.a["title"]

        # Price
        price = book.find(
            "p", class_="price_color"
        ).text.strip()

        # Rating
        rating = book.p["class"][1]

        # Availability
        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        # Product URL
        relative_url = book.h3.a["href"]
        product_url = urljoin(url, relative_url)

        data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product_URL": product_url
        })


# Convert scraped data into DataFrame
df = pd.DataFrame(data)

print("\nTotal books scraped:", len(df))

print("\nFirst 5 records:")
print(df.head())


# Save dataset
df.to_csv("products.csv", index=False)

print("\nDataset saved successfully as products.csv")


# dataset quality check 
print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)