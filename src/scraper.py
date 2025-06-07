# task1_scrape_reviews.py

from google_play_scraper import reviews, Sort
import pandas as pd
from datetime import datetime
# ✅ Updated app package names
bank_apps = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
}

def clean_review_data(raw_reviews, bank_name):
    return [
        {
            "review": r["content"].strip(),
            "rating": r["score"],
            "date": r["at"].strftime("%Y-%m-%d"),
            "bank": bank_name,
            "source": "Google Play"
        }
        for r in raw_reviews if r.get("content") and r.get("score") and r.get("at")
    ]

# Scrape reviews
all_reviews = []
for bank, app_id in bank_apps.items():
    print(f"Scraping reviews for {bank}...")
    reviews_data, _ = reviews(
        app_id,
        lang='en',
        country='us',
        sort=Sort.NEWEST,
        count=450
    )
    all_reviews.extend(clean_review_data(reviews_data, bank))

# Convert to DataFrame and save
df = pd.DataFrame(all_reviews).drop_duplicates(subset=["review", "date", "bank"])
df.to_csv("../data/bank_reviews_cleaned.csv", index=False)
print(f"✅ Saved {len(df)} cleaned reviews to 'bank_reviews_cleaned.csv'")
