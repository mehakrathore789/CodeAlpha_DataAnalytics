# E-Commerce Product Web Scraper

## 📌 Project Overview

This project is developed as part of the **CodeAlpha Data Analytics Internship – Task 1: Web Scraping**.

The objective of this project is to collect publicly available book information from **Books to Scrape** using Python web-scraping techniques. The scraped data is processed using Pandas and stored as a CSV dataset for further analysis.

## 🎯 Objective

* Extract book information from multiple web pages.
* Handle webpage HTML structure using BeautifulSoup.
* Collect relevant product information.
* Create a structured dataset in CSV format.
* Validate the scraped dataset for missing and duplicate records.

## 🌐 Website Used

**Books to Scrape**

https://books.toscrape.com/

## 🛠️ Technologies Used

* **Python**
* **Requests** – To send HTTP requests
* **BeautifulSoup** – To parse HTML content
* **Pandas** – To create and manage the dataset
* **urllib.parse** – To generate complete product URLs
* **VS Code** – Development environment

## 📊 Data Collected

The scraper collects the following information:

| Column       | Description              |
| ------------ | ------------------------ |
| Title        | Name of the book         |
| Price        | Price of the book        |
| Rating       | Rating of the book       |
| Availability | Availability status      |
| Product_URL  | Complete URL of the book |

## 📁 Project Structure

text
Task_1/
│
├── web_scraping.py
├── check_data.py
├── products.csv
├── requirements.txt
└── README.md


## ⚙️ How the Scraper Works

The scraper follows these steps:

1. Sends a request to the website using `Requests`.
2. Receives the webpage HTML.
3. Parses the HTML using `BeautifulSoup`.
4. Identifies book information from the webpage structure.
5. Extracts title, price, rating, availability, and product URL.
6. Stores the extracted information in a Pandas DataFrame.
7. Saves the final dataset as `products.csv`.

The scraper processes **50 pages** of the website.

## 📈 Dataset Result

After scraping:

* **Total Records:** 1000
* **Total Columns:** 5
* **Missing Values:** 0
* **Duplicate Rows:** 0

The final dataset is stored in:

```text
products.csv
```

## 🔍 Data Validation

The `check_data.py` script is used to verify the quality of the scraped dataset.

It checks:

* Dataset shape
* Missing values
* Duplicate records
* Data types
* First few records

## ▶️ How to Run the Project

### 1. Install the required libraries

```bash
pip install -r requirements.txt
```

### 2. Run the web scraper

```bash
python web_scraping.py
```

### 3. Validate the dataset

```bash
python check_data.py
```

## 📄 Output

The scraper generates:


products.csv


containing **1000 scraped book records**.

## 🎓 Learning Outcomes

Through this project, I learned:

* Basics of web scraping
* HTML structure and navigation
* Extracting data using BeautifulSoup
* Handling HTTP requests
* Creating structured datasets using Pandas
* Saving scraped data into CSV files
* Performing basic data-quality checks

## 💼 Internship

**Program:** CodeAlpha Data Analytics Internship
**Task:** Task 1 – Web Scraping
**Project:** E-Commerce Product Web Scraper
