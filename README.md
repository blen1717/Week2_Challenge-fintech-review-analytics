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

  ## Database Setup (SQLite)

This project uses SQLite, a lightweight relational database that supports foreign keys and SQL transactions. The database file fintech_reviews.db is included in the repository.

### Schema

The database contains two tables:

- banks – stores bank names and app names.
- reviews – stores each review with sentiment labels, scores, and identified themes, linked to a bank via bank_id (foreign key).

### Verification Queries

Run the following queries using any SQLite browser or Python to verify data integrity:

`sql
-- Count reviews per bank
SELECT b.bank_name, COUNT(*) FROM reviews r JOIN banks b ON r.bank_id = b.bank_id GROUP BY b.bank_name;

-- Average rating per bank
SELECT b.bank_name, ROUND(AVG(r.rating),2) FROM reviews r JOIN banks b ON r.bank_id = b.bank_id GROUP BY b.bank_name;

## Limitations
- Scraping returned 0 reviews due to regional restrictions; used synthetic dataset as backup.
