# load_to_postgres.py
import psycopg2
import pandas as pd

# Connection parameters – update these with your own PostgreSQL credentials
DB_CONFIG = {
    'host': 'localhost',
    'database': 'fintech_reviews',
    'user': 'postgres',
    'password': 'your_password'
}

def load_data():
    # Load CSV
    df = pd.read_csv('sentiment_thematic_results.csv')
    print(f"Loaded {len(df)} rows")

    # Connect
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # Create tables
    cur.execute("""
        CREATE TABLE IF NOT EXISTS banks (
            bank_id SERIAL PRIMARY KEY,
            bank_name TEXT UNIQUE,
            app_name TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            review_id SERIAL PRIMARY KEY,
            bank_id INTEGER REFERENCES banks(bank_id),
            review_text TEXT,
            rating INTEGER,
            review_date DATE,
            sentiment_label TEXT,
            sentiment_score FLOAT,
            identified_theme TEXT,
            source TEXT
        )
    """)

    # Insert banks
    for bank in df['bank'].unique():
        cur.execute("INSERT INTO banks (bank_name, app_name) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                    (bank, f"{bank} App"))

    # Get bank IDs
    cur.execute("SELECT bank_id, bank_name FROM banks")
    bank_ids = {row[1]: row[0] for row in cur.fetchall()}

    # Insert reviews
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO reviews (bank_id, review_text, rating, review_date,
                                 sentiment_label, sentiment_score, identified_theme, source)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            bank_ids[row['bank']],
            row['review'],
            row['rating'],
            row.get('date', '2024-01-01'),
            row.get('transformer_label', 'NEUTRAL'),
            row.get('transformer_score', 0.0),
            row.get('theme', 'other'),
            'Google Play'
        ))

    conn.commit()
    cur.close()
    conn.close()
    print("Data loaded successfully into PostgreSQL")

if name == "main":
    load_data()
