from google_play_scraper import Sort, reviews
import pandas as pd

def get_reviews(app_id, bank_name, n_reviews=400):
    result, _ = reviews(
        app_id,
        lang='en',
        country='us',
        sort=Sort.NEWEST,
        count=n_reviews
    )
    df = pd.DataFrame(result)
    df = df[['content', 'score', 'at']]
    df.columns = ['review', 'rating', 'date']
    df['bank'] = bank_name
    df['source'] = 'Google Play'
    return df

# Example usage
cbe_app_id = 'com.ethiopian.cbe.mobile'     # replace with actual Play Store ID
# boa_app_id = 'com.abyssinia.bank.app'       # replace with actual Play Store ID
# dashen_app_id = 'com.dashenbank.app'        # replace with actual Play Store ID

# Scrape reviews
cbe_reviews = get_reviews(cbe_app_id, 'Commercial Bank of Ethiopia')
# boa_reviews = get_reviews(boa_app_id, 'Bank of Abyssinia')
# dashen_reviews = get_reviews(dashen_app_id, 'Dashen Bank')

# Combine all
cbe_reviews = pd.concat([cbe_reviews], ignore_index=True)

# Save to CSV
cbe_reviews.to_csv('..data/raw/google_play_reviews.csv', index=False)

print("✅ Reviews scraped and saved.")
