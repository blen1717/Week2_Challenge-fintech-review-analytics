from google_play_scraper import reviews, Sort
import pandas as pd

apps = {
    'CBE': 'com.combanketh.mb.next',
    'BOA': 'com.boa.boaMobileBanking',
    'Dashen': 'com.dashen.dashensuperapp',
}

all_reviews = []
for bank, app_id in apps.items():
    print(f"Scraping {bank}...")
    try:
        result, _ = reviews(app_id, lang='en', country='et', sort=Sort.NEWEST, count=400)
        for r in result:
            all_reviews.append({
                'bank': bank,
                'review': r['content'],
                'rating': r['score'],
                'date': r['at'].date(),
                'source': 'Google Play'
            })
        print(f"  Retrieved {len(result)} reviews")
    except Exception as e:
        print(f"  Failed: {e}")

df = pd.DataFrame(all_reviews)
df.to_csv('reviews.csv', index=False)
print(f"\n✅ Saved {len(df)} reviews to reviews.csv")
