# task2_sentiment_and_theme.py

import pandas as pd
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

nltk.download("punkt")

# Load the preprocessed reviews
df = pd.read_csv("../data/bank_reviews_cleaned.csv")

# Apply sentiment analysis
def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

df["sentiment"] = df["review"].apply(analyze_sentiment)

# Thematic mapping (basic keyword-rule-based)
themes = {
    "login": "Account Access",
    "error": "Account Access",
    "crash": "Reliability",
    "slow": "Performance",
    "transfer": "Performance",
    "ui": "User Interface",
    "interface": "User Interface",
    "support": "Customer Support",
    "help": "Customer Support",
    "feature": "Feature Request",
    "fingerprint": "Feature Request"
}

def extract_themes(text):
    found = set()
    text_lower = text.lower()
    for keyword, theme in themes.items():
        if keyword in text_lower:
            found.add(theme)
    return list(found) if found else ["General"]

df["themes"] = df["review"].apply(extract_themes)

# Save results
df.to_csv("../data/bank_reviews_with_sentiment_and_themes.csv", index=False)
print("✅ Saved annotated reviews to 'bank_reviews_with_sentiment_and_themes.csv'")
