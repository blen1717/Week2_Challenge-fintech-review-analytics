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

  ## Database Setup (PostgreSQL / Neon.tech)

This project uses a PostgreSQL database to store cleaned reviews and analysis results.

### Option A – Local PostgreSQL Installation

1. Download and install PostgreSQL from [postgresql.org](https://www.postgresql.org/download/).
2. During installation, set a password for the postgres user (remember it).
3. Open psql (command line) and run:

`sql
CREATE DATABASE fintech_reviews;
\c fintech_reviews;

## Limitations
- Scraping returned 0 reviews due to regional restrictions; used synthetic dataset as backup.
