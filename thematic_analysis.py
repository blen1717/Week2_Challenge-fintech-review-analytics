# thematic_analysis.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load data
df = pd.read_csv('sentiment_thematic_results.csv')  # or your cleaned CSV

# TF-IDF keywords per bank (optional)
def top_keywords_per_bank(bank_name, n=10):
    subset = df[df['bank']==bank_name]['clean_review'].tolist()
    if not subset:
        return []
    vec = TfidfVectorizer(stop_words='english', max_features=20)
    X = vec.fit_transform(subset)
    words = vec.get_feature_names_out()
    scores = X.sum(axis=0).A1
    word_scores = sorted(zip(words, scores), key=lambda x: x[1], reverse=True)[:n]
    return [w for w, s in word_scores]

# Assign themes
theme_map = {
    'stability': ['crash', 'freeze', 'slow', 'lag', 'error', 'stuck'],
    'account': ['login', 'otp', 'password', 'verify', 'sign'],
    'ux': ['ui', 'interface', 'easy', 'navigation', 'design'],
    'features': ['transfer', 'payment', 'qr', 'fingerprint', 'biometric', 'instant']
}

def assign_theme(text):
    text_lower = str(text).lower()
    for theme, keywords in theme_map.items():
        if any(kw in text_lower for kw in keywords):
            return theme
    return 'other'

df['theme'] = df['clean_review'].apply(assign_theme)
df.to_csv('sentiment_thematic_results.csv', index=False)
print("Thematic analysis complete")
print(df['theme'].value_counts())
