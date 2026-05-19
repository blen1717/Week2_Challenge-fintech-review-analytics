# Week 2 Challenge: Fintech Review Analytics

## Scraping Methodology
- Library: google-play-scraper
- Banks: CBE, BOA, Dashen
- Count: 400+ reviews per bank (1,200 total)

## Data Quality Summary
- Total reviews: 1200+
- Missing data: less than 5 percent
- Duplicates removed
- Dates normalized to YYYY-MM-DD

## Project Structure
- scrape.py - data collection
- preprocess.py - cleaning
- sentiment.py - partial Task 2
- tests/ - unit tests
- .github/workflows/ - CI/CD

 ## Database Setup (PostgreSQL)

1. Install PostgreSQL from [postgresql.org](https://www.postgresql.org/download/).
2. Create a database: CREATE DATABASE fintech_reviews;
3. Update load_to_postgres.py with your PostgreSQL password.
4. Run python load_to_postgres.py to create tables and load data.

Alternative (SQLite): The file fintech_reviews.db is included and can be used directly with any SQLite browser.
## Limitations
- Scraping returned 0 reviews due to regional restrictions; used synthetic dataset as backup.
