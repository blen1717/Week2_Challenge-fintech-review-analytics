"""
scrape.py
Scrapes Google Play reviews for CBE, BOA, Dashen using google-play-scraper.
"""
import pandas as pd
import re

df = pd.read_csv('reviews.csv')
df = df.drop_duplicates(subset=['bank', 'review'])
df = df.dropna(subset=['review', 'rating'])
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
df['clean_review'] = df['review'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', str(x).lower()))
df.to_csv('cleaned_reviews.csv', index=False)
print(f"✅ Cleaned dataset saved. Rows: {len(df)}")
print(df.head())
