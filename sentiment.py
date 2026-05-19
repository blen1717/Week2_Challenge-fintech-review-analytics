"""
scrape.py
Scrapes Google Play reviews for CBE, BOA, Dashen using google-play-scraper.
"""
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
df = pd.read_csv('cleaned_reviews.csv')
df['vader_score'] = df['review'].apply(lambda x: sia.polarity_scores(str(x))['compound'])
df['sentiment'] = df['vader_score'].apply(lambda x: 'positive' if x > 0.05 else ('negative' if x < -0.05 else 'neutral'))
df.to_csv('sentiment_results.csv', index=False)
print("✅ Sentiment analysis complete")
print(df['sentiment'].value_counts())
